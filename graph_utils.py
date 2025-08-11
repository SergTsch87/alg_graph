def bfs(graph_dict, start_vertex):
    if len(graph_dict) <= 1:
        if start_vertex in graph_dict:
            return [start_vertex]
    
    if start_vertex in graph_dict:
        return [start_vertex, graph_dict.get(start_vertex, [])[0]]
    return []