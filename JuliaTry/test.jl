using Dates

function test(a::Time, b::Nothing)::Nothing
    if a
        return a
    end
    return b
end

println(test(Time(0, 0, 0), nothing))