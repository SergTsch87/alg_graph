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


def test_branching_deeper():
    parents = {
        "S": [None],
        "A": ["S"],
        "B": ["S"],
        "C": ["A", "B"],
        "D": ["C"]
    }

    result = build_few_paths(parents, "D")
    assert sorted(result) == sorted([
        ["S", "A", "C", "D"],
        ["S", "B", "C", "D"]
    ])


def test_disconnected_target():
    parents = {
        "A": None,
        "B": []
    }

    assert build_few_paths(parents, "B") == []


def test_target_not_in_parents():
    parents = {"A": None}
    assert build_few_paths(parents, "X") == []


def test_multiple_roots():
    parents = {
        "A": [None],
        "B": [None],
        "C": ["A", "B"]
    }

    result = build_few_paths(parents, "C")
    assert sorted(result) == sorted([
        ["A", "C"],
        ["B", "C"]
    ])


def test_complex_case__multiple_paths():
    parents = {
        "A": [None],
        "B": ["A"],
        "C": ["A"],
        "D": ["B", "C"],
        "E": ["B", "C", "D"]
    }

    result = build_few_paths(parents, "E")
    assert sorted(result) == sorted([
        ["A", "B", "E"],
        ["A", "C", "E"],
        ["A", "B", "D", "E"],
        ["A", "C", "D", "E"]
    ])