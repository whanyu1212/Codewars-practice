import sys

sys.path.insert(0, "/workspaces/Codewars-practice")

import pytest
from src.highest_and_lowest import high_and_low


def test_single_number():
    assert high_and_low("5") == "5 5"


def test_two_numbers():
    assert high_and_low("1 2") == "2 1"


def test_negative_numbers():
    assert high_and_low("-1 -2") == "-1 -2"


def test_mixed_positive_and_negative():
    assert high_and_low("1 -2") == "1 -2"


def test_multiple_numbers():
    assert high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6") == "542 -214"
