import pytest
from graph_utils import build_few_paths


def test_single_node():
    parents = {"A": [None]}
    assert build_few_paths(parents, "A") == [["A"]]


def test_single_chain():
    parents = {
        "A": [None],
        "B": ["A"],
        "C": ["B"]
    }

    assert build_few_paths(parents, "C") == [["A", "B", "C"]]


def test_two_parents_simple():
    parents = {
        "A": [None],
        "B": ["A"],
        "C": ["A"],
        "D": ["B", "C"]
    }

    result = build_few_paths(parents, "D")
    assert sorted(result) == sorted([
        ["A", "B", "D"],
        ["A", "C", "D"]
    ])
