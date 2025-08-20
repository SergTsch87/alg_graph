from collections import deque
# from main import timer


# # Повертає список батьків вершини vertex_parent
# def get_list_parents(vertex_parent, graph_dict):
#     nodes_list = []
#     for node, child in graph_dict.items():
#         if vertex_parent in child:
#             nodes_list.append(node)
#     return nodes_list


# # bfs without addition modules
# # @timer
# # def bfs_list(graph_dict, start_vertex):
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
# def bfs_deque(graph_dict, start_vertex):
def bfs(graph_dict, start_vertex):
    if start_vertex not in graph_dict:
        return []
    
    queue_fifo = deque([start_vertex])
    visited_nodes = [start_vertex]

    while queue_fifo:
        current_vertex = queue_fifo.popleft() # fst
        if graph_dict[current_vertex] != []: # to check a directed graph
            neighbors_list = graph_dict.get(current_vertex, [])  # graph_dict{ current_vertex: neighbors_list }
            for nei in neighbors_list:
                if nei not in visited_nodes:
                    queue_fifo.append(nei) # А чи можна у цій частині тимчасово зробити list(queue_fifo) ? - бо до списку додається швидше, аніж до черги
                    visited_nodes.append(nei)

    return visited_nodes


def dfs(graph_dict, start_vertex):
    visited_nodes = []
    visited_nodes.append(start_vertex)
    
    if len(graph_dict) > 1:
        curr_vertex = graph_dict[start_vertex][0]
        visited_nodes.append(curr_vertex)
    
    return visited_nodes

# "A": ["B"],
# "B": ["A"]