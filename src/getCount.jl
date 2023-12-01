function getCount(s::String)
    vowelsCount = 0
    for char in s
        if char in "aeiou"
            vowelsCount += 1
        end
    end  
    return vowelsCount
end



# function getCount(s::String)
#     return count(char -> char in "aeiou", s)
# end