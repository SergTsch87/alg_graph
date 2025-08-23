#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
import tests.test_graph_utils
import sys
from collections import deque
import time
from graph_utils import dfs

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

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Функція {func.__name__} виконалася за {execution_time} секунд")
        return result
    return wrapper


def get_list_childs(vertex_parent, graph_dict):
    nodes_list = []
    for node, child in graph_dict.items():
        if vertex_parent in child:
            nodes_list.append(node)
    return nodes_list


@timer
def change_iterable(iter_obj, change_method):
    for i in list(iter_obj): # робимо копію, щоб не ламати ітерацію
        change_method(i)
    print(f'len == {len(iter_obj)},  type(iter_obj) == {type(iter_obj)}')


def main():

    # graph_dict = {
    #     "A": ["B"],
    #     "B": ["A"]
    # }

    graph_dict = {
        "A": ["B", "C"],
        "B": ["A"],
        "C": ["A", "D"],
        "D": ["C"]
    }

    visited_nodes = dfs(graph_dict, "A")
    print(f'visited_nodes == {visited_nodes}')

    list_of_graph_dicts = [
        {"A": []},
        {"A": ["B"],"B": ["A"]},
        {"A": ["B"],"B": ["C"],"C": ["A"]},
        {"A": ["B", "C"],"B": ["A"],"C": ["A"]},
        {"A": ["B", "C"],"B": ["A"],"C": ["A", "D", "E", "F"],"D": ["C"],"E": ["C"],"F": ["C"]},
        {"A": ["B", "C", "D", "E", "F"],"B": ["A", "C", "D", "E", "F"],"C": ["A", "B", "D", "E", "F"],"D": ["A", "B", "C", "E", "F"],"E": ["A", "B", "C", "D", "F"],"F": ["A", "B", "C", "D", "E"]},
        {},
        {"A": ["B", "C"],"B": ["C", "A"],"C": ["A", "B"]},
        {"A": ["B", "C", "D"],"B": ["A"],"C": ["A"],"D": ["A"]},
        {"A": ["B"],"B": ["A"],"C": []},
        {"A": ["B", "C"],"B": ["A", "C"],"C": ["A", "B"],"D": ["E", "F"],"E": ["D", "F"],"F": ["D", "E"]},
        {"A": ["B"],"B": []},
        {"A": ["A"]},
        {"A": ["B", "C"],"B": ["A"],"C": ["A", "D", "E", "F", "G", "H", "K", "L", "M", "N", "O", "P", "Q"],"D": ["C"],"E": ["C"],"F": ["C"],"G": ["C"],"H": ["C"],"K": ["C"],"L": ["C"],"M": ["C"],"N": ["C"],"O": ["C"],"P": ["C"],"Q": ["C"]},
        {"A": ["B"],"B": ["A"]},
        {"A": ["B", "B"],"B": ["A"]},
        {"A": [],"B": []}
    ]

    # len_for_iter_objs = 100000
    # list_1 = [i for i in range(len_for_iter_objs)]
    # quque_2 = deque( range(len_for_iter_objs) )
    
    # change_iterable(list_1, list_1.append)
    # change_iterable(list_1, list_1.remove)
    # print('\n')
    # change_iterable(quque_2, quque_2.append)
    # change_iterable(quque_2, lambda _: quque_2.popleft())


    # len_for_iter_objs = 100000
    # list_1 = [i for i in range(len_for_iter_objs)]
    
    # change_iterable(list_1, list_1.append)
    # print('\n')
    # quque_2 = deque(list_1)
    # change_iterable(quque_2, lambda _: quque_2.popleft())


    # graph_dict = {
    #     "A": ["B"],
    #     "B": ["A"],
    #     "C": ["A"]
    # }

    # # list_node = get_list_childs("A", graph_dict)
    # # print(list_node)

    # # queue_fifo = get_list_childs("A", graph_dict).reverse()
    # queue_fifo = get_list_childs("A", graph_dict)
    # queue_fifo.reverse()
    # print(queue_fifo)
    # print(queue_fifo[-1])

    # # my_list = [2, 4, 1]
    # # while my_list:
    # #     print(my_list)
    # #     my_list.pop()
    # # print([2, 4, 1][-1])
    # # graph_dict = {
    # #     "A": ["B"]
    # # }

    # # # print( graph_dict["A"] )
    # # print( graph_dict.get("A", [])[0] )

    # # # print(sys.path)

if __name__ == '__main__':
    main()