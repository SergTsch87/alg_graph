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


def bfs_with_parents(graph_dict, start_vertex):
    if start_vertex not in graph_dict:
        return [], {}
    
    queue_fifo = deque([start_vertex])
    visited_nodes = [start_vertex]
    parents = {start_vertex: [None]}

    while queue_fifo:
        current_vertex = queue_fifo.popleft() # fst
        if graph_dict[current_vertex] != []: # to check a directed graph
            neighbors_list = graph_dict.get(current_vertex, [])  # graph_dict{ current_vertex: neighbors_list }
            # print('\nInput for nei:')
            # print(f'! current_vertex: {current_vertex}')
            # print(f'neighbors_list: {neighbors_list}')
            for nei in neighbors_list:
                # print(f'nei: {nei}')
                # print(f'parents: {parents}')
                # print(f'visited_nodes: {visited_nodes}')
                
                if nei not in parents:
                    parents[nei] = []
                
                # if ( current_vertex not in parents[nei] ): # для додавання всіх(!) вузлів до parents[nei]
                # if ( nei not in visited_nodes ): # для додавання першого вузла до parents[nei]
                # if ( nei in queue_fifo ): # для додавання правильних значень до parents, але тільки тих, які займають 2-ге та наступні місця у списку
                if ( nei not in visited_nodes ) or ( nei in queue_fifo ):
                    parents[nei].append(current_vertex)
                    # print(f'parents[{nei}]: {parents[nei]}')
                
                if nei not in visited_nodes:
                    queue_fifo.append(nei) # А чи можна у цій частині тимчасово зробити list(queue_fifo) ? - бо до списку додається швидше, аніж до черги
                    visited_nodes.append(nei)
                
            # print('Output for nei\n')

    return visited_nodes, parents


# # target vs goal
# # Побудова одного шляху для parents, значеннями ключів якого є окремі числа, а не списки
# def build_path(parents, target):
#     if target not in parents:
#         return []
    
#     path = []
    
#     reversed_parents = dict(reversed(parents.items()))
#     # print(f'reversed_parents = {reversed_parents}')
#     val_tmp = ""

#     for key, val in reversed_parents.items():
#         if ( key == target ) or ( key == val_tmp ):
#             path.append(key)
#             # print(f'key = {key}: path = {path}')
#             if val is None:
#                 break
#             val_tmp = val

#     # print(f'"path" after for loop == {path}')
    
#     path.reverse()
#     # print(f'"path" after used "reverse()" == {path}')
#     return path


# def build_few_paths(parents, target):
#     if target not in parents:
#         return []
    
#     paths_list = []
#     stack = [[target]] # працюємо зі стеком шляхів
    
#     while stack:
#         path = stack.pop()
#         last = path[-1]

#         # коли дійшли до кореня
#         if ( parents[last] == [None] ) or ( parents[last] is None ):
#             paths_list.append(path)
#         else:
#             for p in parents[last]:
#                 stack.append(path + [p])

#     # розгортаємо, бо будували у напрямку target -> root
#     return [list(reversed(p)) for p in paths_list]


def build_few_paths(parents, target):
    if target not in parents:
        return []
    
    reversed_parents = dict(reversed(parents.items()))
    paths_list = []

    for node in reversed_parents[target]: # [B, C]
        path = [target]
        val_tmp = node # стартуємо з поточного "кандидата" батька

        for key, val in reversed_parents.items():
            if key == val_tmp:
                path.append(key)
                if ( val is None ) or ( val == [None] ):
                    break
                
                val_tmp = val[0] # беремо першого (поки що)

        path.reverse()
        paths_list.append(path)
    
    return paths_list


    # parents = {
    #     "A": None,
    #     "B": ["A"],
    #     "C": ["B"]
    # }

    # >> [["A", "B", "C"]]


    # parents = {
    #     "A": None,
    #     "B": ["A"],
    #     "C": ["A"],
    #     "D": ["B", "C"]
    # }

    # result = build_few_paths(parents, "D")
    # assert sorted(result) == sorted([
    #     [["A", "B", "D"]],
    #     [["A", "C", "D"]]
    # ])