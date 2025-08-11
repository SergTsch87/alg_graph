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


if __name__ == '__main__':
    pytest.main()