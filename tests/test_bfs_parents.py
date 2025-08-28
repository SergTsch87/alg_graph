import pytest
from graph_utils import bfs_with_parents


def test_parents_single_node():
    graph_dict = {
        "A": []
    }

    assert bfs_with_parents(graph_dict, "A") == (["A"], {"A": None})


def test_parents_two_nodes_edge():
    graph_dict = {
        "A": ["B"],
        "B": ["A"]
    }

    assert bfs_with_parents(graph_dict, "A") == (
        ["A", "B"],
        {"A": None, "B": "A"}
    )


def test_three_nodes_edges():
    graph_dict = {
        "A": ["B"],
        "B": ["C"],
        "C": ["A"]
    }

    assert bfs_with_parents(graph_dict, "A") == (
        ["A", "B", "C"],
        {"A": None, "B": "A", "C": "B"}
    )


def test_three_nodes_two_siblings_from_root():
    graph_dict = {
        "A": ["B", "C"],
        "B": ["A"],
        "C": ["A"]
    }

    assert bfs_with_parents(graph_dict, "A") == (
        ["A", "B", "C"],
        {"A": None, "B": "A", "C": "A"}
    )


def test_branching_deeper_from_C():
    graph_dict = {
        "A": ["B", "C"],
        "B": ["A"],
        "C": ["A", "D", "E", "F"],
        "D": ["C"],
        "E": ["C"],
        "F": ["C"]
    }

    assert bfs_with_parents(graph_dict, "A") == (
        ["A", "B", "C", "D", "E", "F"],
        {"A": None,
         "B": "A",
         "C": "A",
         "D": "C",
         "E": "C",
         "F": "C"}
    )


def test_full_graph():
    graph_dict = {
        "A": ["B", "C", "D", "E", "F"],
        "B": ["A", "C", "D", "E", "F"],
        "C": ["A", "B", "D", "E", "F"],
        "D": ["A", "B", "C", "E", "F"],
        "E": ["A", "B", "C", "D", "F"],
        "F": ["A", "B", "C", "D", "E"]
    }

    assert bfs_with_parents(graph_dict, "A") == (
        ["A", "B", "C", "D", "E", "F"],
        {"A": None,
         "B": "A",
         "C": "A",
         "D": "A",
         "E": "A",
         "F": "A"}
    )


# Додаткові тести
def test_missing_node():
    graph_dict = {}

    assert bfs_with_parents(graph_dict, "A") == ([], {})


def test_cyclic_graph():
    graph_dict = {
        "A": ["B", "C"],
        "B": ["C", "A"],
        "C": ["A", "B"]
    }

    assert bfs_with_parents(graph_dict, "A") == (
        ["A", "B", "C"],
        {"A": None, "B": "A", "C": "A"}
    )


def test_star_graph():
    graph_dict = {
        "A": ["B", "C", "D"],
        "B": ["A"],
        "C": ["A"],
        "D": ["A"]
    }

    assert bfs_with_parents(graph_dict, "A") == (
        ["A", "B", "C", "D"],
        {"A": None,
         "B": "A",
         "C": "A",
         "D": "A"}
    )


def test_graph_with_isolate_vertex():
    graph_dict = {
        "A": ["B"],
        "B": ["A"],
        "C": []
    }

    assert bfs_with_parents(graph_dict, "A") == (
        ["A", "B"],
        {"A": None, "B": "A"}
    )


def test_unconnected_graph():
    graph_dict = {
        "A": ["B", "C"],
        "B": ["A", "C"],
        "C": ["A", "B"],
        "D": ["E", "F"],
        "E": ["D", "F"],
        "F": ["D", "E"]
    }

    assert bfs_with_parents(graph_dict, "A") == (
        ["A", "B", "C"],
        {"A": None, "B": "A", "C": "A"}
    )


def test_direct_graph():
    graph_dict = {
        "A": ["B"],
        "B": []
    }

    assert bfs_with_parents(graph_dict, "B") == (
        ["B"],
        {"B": None}
    )


def test_loop_graph():
    graph_dict = {
        "A": ["A"]
    }

    assert bfs_with_parents(graph_dict, "A") == (
        ["A"],
        {"A": None}
    )


def test_graph_with_many_children():
    graph_dict = {
        "A": ["B", "C"],
        "B": ["A"],
        "C": ["A", "D", "E", "F", "G", "H", "K", "L", "M", "N", "O", "P", "Q"],
        "D": ["C"],
        "E": ["C"],
        "F": ["C"],
        "G": ["C"],
        "H": ["C"],
        "K": ["C"],
        "L": ["C"],
        "M": ["C"],
        "N": ["C"],
        "O": ["C"],
        "P": ["C"],
        "Q": ["C"]
    }

    assert bfs_with_parents(graph_dict, "A") == (
        ["A", "B", "C", "D", "E", "F", "G", "H", "K", "L", "M", "N", "O", "P", "Q"],
        {"A": None,
         "B": "A",
         "C": "A",
         "D": "C",
         "E": "C",
         "F": "C",
         "G": "C",
         "H": "C",
         "K": "C",
         "L": "C",
         "M": "C",
         "N": "C",
         "O": "C",
         "P": "C",
         "Q": "C"}
    )


def test_start_from_empty_node():
    graph_dict = {
        "A": ["B"],
        "B": ["A"]
    }

    assert bfs_with_parents(graph_dict, "C") == (
        [],
        {}
    )


def test_graph_with_duplicate_edges():
    graph_dict = {
        "A": ["B", "B"],
        "B": ["A"]
    }

    assert bfs_with_parents(graph_dict, "A") == (
        ["A", "B"],
        {"A": None, "B": "A"}
    )


def test_isolated_vertex():
    graph_dict = {
        "A": [],
        "B": []
    }

    assert bfs_with_parents(graph_dict, "A") == (["A"], {"A": None})