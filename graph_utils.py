from collections import deque
# from main import timer


# bfs with deque module
def bfs(graph_dict, start_vertex):#, parents):
    if start_vertex not in graph_dict:
        return []#, []
    
    queue_fifo = deque([start_vertex])
    visited_nodes = [start_vertex]
    # parents = []

    while queue_fifo:
        current_vertex = queue_fifo.popleft() # fst
        if graph_dict[current_vertex] != []: # to check a directed graph
            neighbors_list = graph_dict.get(current_vertex, [])  # graph_dict{ current_vertex: neighbors_list }
            for nei in neighbors_list:
                if nei not in visited_nodes:
                    queue_fifo.append(nei) # А чи можна у цій частині тимчасово зробити list(queue_fifo) ? - бо до списку додається швидше, аніж до черги
                    visited_nodes.append(nei)

    return visited_nodes#, parents


def dfs(graph_dict, start_vertex):
    if start_vertex not in graph_dict:
        return []
    
    queue_lifo = deque([ start_vertex ])
    visited_nodes = []

    while queue_lifo:
        current_vertex = queue_lifo.pop()
        if current_vertex not in visited_nodes:
            visited_nodes.append(current_vertex)
            neighbors = graph_dict[current_vertex]
            queue_lifo.extend(reversed(neighbors))

    return visited_nodes