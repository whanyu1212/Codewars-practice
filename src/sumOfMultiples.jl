"""
    sumOfMultiples(number::Int)

Return the sum of all numbers less than `number` that are multiples of 3 or 5.

# Arguments
- `number::Int`: The upper limit for the sum (exclusive).

# Returns
- `Int`: The sum of all multiples of 3 or 5 less than `number`.
"""
function sumOfMultiples(number::Int)::Int
    return filter(x -> x % 3 == 0 || x % 5 == 0, 1:number-1) |> sum
end