#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
import tests.test_graph_utils
import sys

# -----------------------------------------------------------------------------
# GLOBALS
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# CONSTANTS
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# LOCAL UTILITIES
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# FUNCTIONS
# -----------------------------------------------------------------------------
def get_list_childs(vertex_parent, graph_dict):
    nodes_list = []
    for node, child in graph_dict.items():
        if vertex_parent in child:
            nodes_list.append(node)
    return nodes_list
        

def main():
    graph_dict = {
        "A": ["B"],
        "B": ["A"],
        "C": ["A"]
    }

    # list_node = get_list_childs("A", graph_dict)
    # print(list_node)

    # queue_fifo = get_list_childs("A", graph_dict).reverse()
    queue_fifo = get_list_childs("A", graph_dict)
    queue_fifo.reverse()
    print(queue_fifo)
    print(queue_fifo[-1])

    # my_list = [2, 4, 1]
    # while my_list:
    #     print(my_list)
    #     my_list.pop()
    # print([2, 4, 1][-1])
    # graph_dict = {
    #     "A": ["B"]
    # }

    # # print( graph_dict["A"] )
    # print( graph_dict.get("A", [])[0] )

    # # print(sys.path)

if __name__ == '__main__':
    main()