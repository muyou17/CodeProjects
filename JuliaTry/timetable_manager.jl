using Dates, Serialization, DataFrames


function get_options_input(options::Tuple{Vararg{String}})::String
    println()
    for (index, option) in enumerate(options)
        println("$index. $option")
    end
    print("Select an option: ")
    return readline()
end


function is_valid_time_component(component::SubString{String}, max_value::Int)::Bool
    try
        value = parse(Int, component)
        return <= value <= max_value
    catch
        return false
    end
end


function get_time_input(prompt::String)::Union{Time, Nothing}
    while true
        print("\n$prompt ")
        input = readline()
        if occursin(r"^(q|quit)$"i, input)
            exit(0)
        elseif occursin(r"^(b|back)$"i, input)
            return nothing
        end

        time_components = split(input)
        if length(time_components) == 1
            push!(time_components, "0")
        end
        if length(time_components) != 2
            println("Invalid input! Enter exactly 2 components: HH MM.")
            continue
        elseif !is_valid_time_component(time_components[1], 23)
            println("Invalid hour! Enter an integer from 0 to 23.")
            continue
        elseif !is_valid_time_component(time_components[2], 59)
            println("Invalid minute! Enter an integer from 0 to 59.")
            continue
        end

        hour = parse(Int, time_components[1])
        minute = parse(Int, time_components[2])
        return Time(hour, minute)
    end
end


function get_day_range_input()::Union{Tuple{Time, Time}, Nothing}
    while true
        wake_up_time = nothing
        while true
            wake_up_time = get_time_input("When do you wake up?")
            if isnothing(wake_up_time)
                return nothing
            end

            time_string = Dates.format(wake_up_time, "HH:MM")
            print("Are you sure you want to wake up at $time_string? ")
            confirmation = readline()
            if occursin(r"^(|y|yes)$"i, confirmation)
                break
            elseif occursin(r"^(n|no|b|back)$"i, confirmation)
                continue
            elseif occursin(r"^(q|quit)$"i, confirmation)
                exit(0)
            else
                println("Invalid input!")
            end
        end

        while true
            bed_time = get_time_input("When do you go to bed?")
            if isnothing(bed_time)
                break
            elseif bed_time <= wake_up_time
                println("Invalid input! Bed time cannot be sooner or the same as wake up time.")
                continue
            end

            time_string = Dates.format(bed_time, "HH:MM")
            print("Are you sure you want to go to bed at $time_string? ")
            confirmation = readline()
            if occursin(r"^(|y|yes)$"i, confirmation)
                return wake_up_time, bed_time
            elseif occursin(r"^(n|no|b|back)$"i, confirmation)
                continue
            elseif occursin(r"^(q|quit)$"i, confirmation)
                exit(0)
            else
                println("Invalid input!")
            end
        end
    end
end


function get_duration_input(max_duration::Minute)::Union{Minute, Nothing}
    while true
        print("Task duration: ")
        input = readline()
        if occursin(r"^(b|back)$"i, input)
            return nothing
        elseif occursin(r"^(q|quit)$"i, input)
            exit(0)
        end
        try
            duration = Minute(parse(Int, input))
            if !(max_duration >= duration >= Minute(0))
                throw(AssertionError)
            elseif get_confirmation_input(duration, "duration")
                return duration
            end
        catch
            println("Invalid input! Enter an integer from 0 to $(max_duration.value).")
        end
    end
end


function get_confirmation_input(input::Union{Time, String, Minute}, type::String)::Bool
    while true
        if type == "task"
            print("Proceed with \"$input\"? ")
            confirmation = readline()
        elseif type == "duration"
            print("Do you want to do it in $input? ")
            confirmation = readline()
        else
            return false
        end
        if occursin(r"^(|y|yes)$"i, confirmation)
            return true
        elseif occursin(r"^(n|no|b|back)$"i, confirmation)
            return false
        elseif occursin(r"^(q|quit)$"i, confirmation)
            exit(0)
        else
            println("Invalid input!")
        end
    end
end


function get_next_row_input(previous_time::Time,
                            previous_duration::Minute,
                            bed_time::Time)::Union{Tuple{Time, String, Minute}, Nothing}
    time = previous_time + previous_duration
    time_string = Dates.format(time, "HH:MM")
    while true
        println("\nWhat do you want to do at $time_string?")
        print("Task name: ")
        task = readline()
        if occursin(r"^(b|back)$"i, task)
            return nothing
        elseif occursin(r"^(q|quit)$"i, task)
            exit(0)
        elseif get_confirmation_input(task, "task")
            break
        end
        while true
            duration = get_duration_input(Minute(bed_time - time))
            if isnothing(duration)
                break
            elseif get_confirmation_input(duration, "duration")
                return time, task, duration
            end
        end
    end
end


function write_new_table()::Nothing
    day_range = get_day_range_input()
    if isnothing(day_range)
        return nothing
    end

    time, bed_time = day_range
    index, task, duration = 1, "Wake up", Minute(0)
    timetable = Dict(
        "Index" => [index],
        "Time" => [time],
        "Task" => [task],
        "Duration" => [duration]
    )

    while task != "Go to bed"
        index += 1
        time, task, duration = get_next_row_input(time, duration, bed_time)
        break
    end
end


function main()::Nothing
    options = (
        "Show current task",
        "Show a timetable",
        "Write a new timetable",
        "Modify an existing timetable",
        "Export a timetable to CSV file",
        "Import a CSV file to the program",
        "Exit the program"
    )

    while true
        selection = get_options_input(options)
        if selection == "3"
            write_new_table()
        elseif occursin(r"^(q|quit|7)$"i, selection)
            exit(0)
        else
            println("Invalid input!")
        end
    end
end


println(
"You are running Timetable Manager, a timetable management program developed by Muyō.
During any input prompt, you can type \"quit\" to exit the program immediately,
                                 type \"back\" to return to the previous prompt."
)

main()