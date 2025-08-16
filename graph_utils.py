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

    # queue_fifo = []
    # visited_nodes = []

    queue_fifo = [start_vertex]
    visited_nodes = [start_vertex]
    # current_vertex = queue_fifo.pop(0)
    # neighbors_list = get_list_childs(current_vertex, graph_dict)

    while queue_fifo:
        current_vertex = queue_fifo.pop(0)
        # queue_fifo.extend(neighbors_list)
        # visited_nodes.extend(neighbors_list)
        neighbors_list = get_list_childs(current_vertex, graph_dict)
        for item in neighbors_list:
            if item not in visited_nodes:
                queue_fifo.append(item)
                visited_nodes.append(item)
        

    # visited_nodes = [start_vertex]
    # queue_fifo = get_list_childs(start_vertex, graph_dict)
    # queue_fifo.reverse()

    # while queue_fifo:
    #     start_vertex = queue_fifo.pop()
    #     visited_nodes.append(start_vertex)
        
    #     temp_queue_fifo = get_list_childs(start_vertex, graph_dict)
    #     temp_queue_fifo.reverse()
    #     queue_fifo.append(temp_queue_fifo)

    return visited_nodes