def get_list_childs(vertex_parent, graph_dict):
    nodes_list = []
    for node, child in graph_dict.items():
        if vertex_parent in child:
            nodes_list.append(node)
    return nodes_list


def bfs(graph_dict, start_vertex):
    if start_vertex not in graph_dict:
        return []
    
    if len(graph_dict) <= 1:
        if start_vertex in graph_dict:
            return [start_vertex]

    queue_fifo = [start_vertex]
    visited_nodes = [start_vertex]

    while queue_fifo:
        current_vertex = queue_fifo.pop(0)
        neighbors_list = get_list_childs(current_vertex, graph_dict)
        for item in neighbors_list:
            if item not in visited_nodes:
                queue_fifo.append(item)
                visited_nodes.append(item)        

    return visited_nodes