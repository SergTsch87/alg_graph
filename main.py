#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------


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
def main():
    
    # Adjacency list of graph:
    graph_dict = {
        "A": ["D", "B"],
        "B": ["A", "C", "E"],
        "C": ["B"],
        "D": ["A"],
        "E": ["B"]
    }

    visited_nodes_list = []
    queue_fifo_list = []
    current_vertex = ""

    # Initial
    current_vertex = "A"
    visited_nodes_list.append(current_vertex)

    # Added all neighbors of current_vertex vertex
    for item in graph_dict[current_vertex][::-1]:
        queue_fifo_list.append(item)

    print(f'visited_nodes_list == {visited_nodes_list}')
    print(f'queue_fifo_list == {queue_fifo_list}')
    print(f'current_vertex == {current_vertex}')


    # Next step
    current_vertex = graph_dict[current_vertex][0]
    visited_nodes_list.append(current_vertex)
    queue_fifo_list = queue_fifo_list[:-1]

    # Added all neighbors of current_vertex vertex
    for item in graph_dict[current_vertex][::-1]:
        queue_fifo_list.append(item)

    print(f'visited_nodes_list == {visited_nodes_list}')
    print(f'queue_fifo_list == {queue_fifo_list}')
    print(f'current_vertex == {current_vertex}')
    

if __name__ == '__main__':
    main()