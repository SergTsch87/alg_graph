import pytest
from graph_utils import bfs


def test_single_node():
    graph_dict = {
        "A": []
    }

    assert bfs(graph_dict, "A") == ["A"]


def test_two_nodes_edge():
    graph_dict = {
        "A": ["B"],
        "B": ["A"]
    }

    assert bfs(graph_dict, "A") == ["A", "B"]


def test_three_nodes_edges():
    graph_dict = {
        "A": ["B"],
        "B": ["A"],
        "C": ["A"]
    }

    assert bfs(graph_dict, "A") == ["A", "B", "C"]


def test_three_nodes_two_siblings_from_root():
    graph_dict = {
        "A": ["B", "C"],
        "B": ["A"],
        "C": ["A"]
    }

    assert bfs(graph_dict, "A") == ["A", "B", "C"]


def test_branching_deeper_from_C():
    graph_dict = {
        "A": ["B", "C"],
        "B": ["A"],
        "C": ["A", "D", "E", "F"],
        "D": ["C"],
        "E": ["C"],
        "F": ["C"]
    }

    assert bfs(graph_dict, "A") == ["A", "B", "C", "D", "E", "F"]


if __name__ == '__main__':
    pytest.main()