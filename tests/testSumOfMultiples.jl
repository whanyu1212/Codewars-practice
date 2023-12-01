using Test
include("../src/sumOfMultiples.jl")

@testset "sumOfMultiples tests" begin
    @test sumOfMultiples(10) == 23
    @test sumOfMultiples(20) == 78
    @test sumOfMultiples(0) == 0
    @test sumOfMultiples(3) == 0
end