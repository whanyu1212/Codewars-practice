using Test
include("../src/getCount.jl")

@testset "getCount tests" begin
    @test getCount("hello") == 2
    @test getCount("world") == 1
    @test getCount("aeiou") == 5
    @test getCount("bcdfg") == 0
end