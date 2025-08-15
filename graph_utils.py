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
    
    visited_nodes = [start_vertex]
    queue_fifo = get_list_childs(start_vertex, graph_dict)
    queue_fifo.reverse()
    # print(queue_fifo)
    # print(queue_fifo[-1])

    start_vertex = queue_fifo[-1]
    last_el = queue_fifo.pop()
    visited_nodes.append(last_el)

    if queue_fifo:
        start_vertex = queue_fifo[-1]
        last_el = queue_fifo.pop()
        visited_nodes.append(last_el)

    # Повинно бути:
        # start_vertex == "C"
        # queue_fifo == []
        # visited_nodes == [ABC]
    print(start_vertex)
    print(queue_fifo)
    print(visited_nodes)

    return visited_nodes

    # queue_fifo = get_list_childs("A", graph_dict).reverse()
    
    # if start_vertex in graph_dict: # len(graph_dict) > 2
    #     while queue_fifo: # доки черга не порожня
    #         visited_nodes.append(queue_fifo[0]) # Потрібен саме останній елемент queue_fifo !
    #         for vertex in graph_dict:
    #             if vertex != start_vertex and vertex not in visited_nodes:
    #                 # queue_fifo.append(graph_dict.get(vertex, ""))
    #                 queue_fifo.append(vertex)

    #         if queue_fifo[0] == start_vertex:
    #             queue_fifo = []

        # return [start_vertex, graph_dict.get(start_vertex, [])[0]]
        # return visited_nodes