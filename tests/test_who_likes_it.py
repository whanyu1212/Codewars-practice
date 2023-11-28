import sys

sys.path.insert(0, "/workspaces/Codewars-practice")

import pytest
from src.who_likes_it import names_to_text


def test_no_likes():
    assert names_to_text([]) == "no one likes this"


def test_one_like():
    assert names_to_text(["Peter"]) == "Peter likes this"


def test_two_likes():
    assert names_to_text(["Jacob", "Alex"]) == "Jacob and Alex like this"


def test_three_likes():
    assert names_to_text(["Max", "John", "Mark"]) == "Max, John and Mark like this"


def test_more_than_three_likes():
    assert (
        names_to_text(["Alex", "Jacob", "Mark", "Max"])
        == "Alex, Jacob and 2 others like this"
    )
