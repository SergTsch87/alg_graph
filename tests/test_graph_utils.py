import pytest
from graph_utils import bfs


def test_single_node():
    graph_dict = {
        "A": []
    }

    assert bfs(graph_dict, "A") == ["A"]


if __name__ == '__main__':
    pytest.main()