from collections import deque


# Повертає список батьків вершини vertex_parent
def get_list_parents(vertex_parent, graph_dict):
    nodes_list = []
    for node, child in graph_dict.items():
        if vertex_parent in child:
            nodes_list.append(node)
    return nodes_list


# # bfs without addition modules
# def bfs(graph_dict, start_vertex):
#     if start_vertex not in graph_dict:
#         return []
    
#     queue_fifo = [start_vertex]
#     visited_nodes = [start_vertex]

#     while queue_fifo:
#         current_vertex = queue_fifo.pop(0)
#         if graph_dict[current_vertex] != []: # to check a directed graph
#             neighbors_list = get_list_parents(current_vertex, graph_dict)
#             for item in neighbors_list:
#                 if item not in visited_nodes:
#                     queue_fifo.append(item)
#                     visited_nodes.append(item)        

#     return visited_nodes


# bfs with deque module
def bfs(graph_dict, start_vertex):
    if start_vertex not in graph_dict:
        return []
    
    queue_fifo = deque([start_vertex])
    visited_nodes = [start_vertex]
    # queue = deque()

    while queue_fifo:
        current_vertex = queue_fifo.popleft() # fst
        if graph_dict[current_vertex] != []: # to check a directed graph
            neighbors_list = get_list_parents(current_vertex, graph_dict)
            for item in neighbors_list:
                if item not in visited_nodes:
                    queue_fifo.append(item)
                    visited_nodes.append(item)        

    return visited_nodes