import pytest
from graph_utils import build_path


def test_parents_single_node():
    parents = {"A": None}
    assert build_path(parents, "A") == ["A"]


def test_parents_two_nodes_direct_edge():
    parents = {
        "A": None,
        "B": "A"
    }

    assert build_path(parents, "B") == ["A", "B"]


def test_parents_three_nodes_line(): # cycle but BFS parents
    parents = {
        "A": None,
        "B": "A",
        "C": "B"
    }

    assert build_path(parents, "C") == ["A", "B", "C"]


def test_parents_target_is_the_root():
    parents = {
        "A": None,
        "B": "A"
    }
    assert build_path(parents, "A") == ["A"]


def test_parents_branching_graph(): # diamond shape
    parents = {
        "A": None,
        "B": "A",
        "C": "A",
        "D": "B"
    }

    assert build_path(parents, "D") == ["A", "B", "D"]


def test_parents_disconnected_node(): # not in parents
    parents = {
        "A": None,
        "B": "A"
    }

    assert build_path(parents, "C") == []


def test_parents_four_nodes_line():
    parents = {
        "A": None,
        "B": "A",
        "C": "B",
        "D": "C"
    }

    assert build_path(parents, "D") == ["A", "B", "C", "D"]


def test_parents_multiple_siblings(): # as diamond shape
    parents = {
        "A": None,
        "B": "A",
        "C": "A",
        "D": "C"
    }

    assert build_path(parents, "D") == ["A", "C", "D"]


def test_parents_path_reconstruction_when_target_is_child_of_root():
    parents = {
        "A": None,
        "B": "A",
        "C": "B"
    }

    assert build_path(parents, "B") == ["A", "B"]


def test_parents_no_parents_at_all():
    parents = {}
    assert build_path(parents, "X") == []