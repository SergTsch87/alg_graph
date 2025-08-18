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
        "A": ["B", "C"],
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


def test_full_graph():
    graph_dict = {
        "A": ["B", "C", "D", "E", "F"],
        "B": ["A", "C", "D", "E", "F"],
        "C": ["A", "B", "D", "E", "F"],
        "D": ["A", "B", "C", "E", "F"],
        "E": ["A", "B", "C", "D", "F"],
        "F": ["A", "B", "C", "D", "E"]
    }

    assert bfs(graph_dict, "A") == ["A", "B", "C", "D", "E", "F"]


# Додаткові тести
def test_missing_node():
    graph_dict = {}

    assert bfs(graph_dict, "A") == []


def test_cyclic_graph():
    graph_dict = {
        # "A": ["B"],
        # "B": ["C"],
        # "C": ["A"]
        "A": ["B", "C"],
        "B": ["C", "A"],
        "C": ["A", "B"]
    }

    assert bfs(graph_dict, "A") == ["A", "B", "C"]


def test_star_graph():
    graph_dict = {
        "A": ["B", "C", "D"],
        "B": ["A"],
        "C": ["A"],
        "D": ["A"]
    }

    assert bfs(graph_dict, "A") == ["A", "B", "C", "D"]


def test_graph_with_isolate_vertex():
    graph_dict = {
        "A": ["B"],
        "B": ["A"],
        "C": []
    }

    assert bfs(graph_dict, "A") == ["A", "B"]


def test_unconnected_graph():
    graph_dict = {
        "A": ["B", "C"],
        "B": ["A", "C"],
        "C": ["A", "B"],
        "D": ["E", "F"],
        "E": ["D", "F"],
        "F": ["D", "E"]
    }

    assert bfs(graph_dict, "A") == ["A", "B", "C"]


def test_direct_graph():
    graph_dict = {
        "A": ["B"],
        "B": []
    }

    assert bfs(graph_dict, "B") == ["B"]


def test_loop_graph():
    graph_dict = {
        "A": ["A"]
    }

    assert bfs(graph_dict, "A") == ["A"]


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

    assert bfs(graph_dict, "A") == ["A", "B", "C", "D", "E", "F", "G", "H", "K", "L", "M", "N", "O", "P", "Q"]


def test_start_from_empty_node():
    graph_dict = {
        "A": ["B"],
        "B": ["A"]
    }

    # assert bfs(graph_dict, "C") == ["A", "B", "C"] # -> Red
    assert bfs(graph_dict, "C") == [] # -> Green


def test_graph_with_duplicate_edges():
    graph_dict = {
        "A": ["B", "B"],
        "B": ["A"]
    }

    assert bfs(graph_dict, "A") == ["A", "B"]


if __name__ == '__main__':
    pytest.main()