from collections import deque
import heapq


# bfs with deque module
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
            for nei in neighbors_list:
                if nei not in parents:
                    parents[nei] = []                
                # if ( current_vertex not in parents[nei] ): # для додавання всіх(!) вузлів до parents[nei]
                # if ( nei not in visited_nodes ): # для додавання першого вузла до parents[nei]
                # if ( nei in queue_fifo ): # для додавання правильних значень до parents, але тільки тих, які займають 2-ге та наступні місця у списку
                if ( nei not in visited_nodes ) or ( nei in queue_fifo ):
                    parents[nei].append(current_vertex)
                
                if nei not in visited_nodes:
                    queue_fifo.append(nei) # А чи можна у цій частині тимчасово зробити list(queue_fifo) ? - бо до списку додається швидше, аніж до черги
                    visited_nodes.append(nei)

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


# with stack
def build_few_paths(parents, target):
    if target not in parents:
        return []
    
    paths_list = []
    stack = [[target]] # працюємо зі стеком шляхів

    while stack:
        path = stack.pop()
        last = path[-1]

        # коли дійшли до кореня
        if ( parents[last] == [None] ) or ( parents[last] is None ):
            paths_list.append(path)            
        else:
            for p in parents[last]:
                stack.append(path + [p])

    # розгортаємо, бо будували у напрямку target -> root
    return [list(reversed(p)) for p in paths_list]


# without stack
# def build_few_paths(parents, target):
#     if target not in parents:
#         return []
    
#     reversed_parents = dict(reversed(parents.items()))
#     paths_list = []

#     for node in reversed_parents[target]: # [B, C]
#         path = [target]
#         val_tmp = node # стартуємо з поточного "кандидата" батька

#         for key, val in reversed_parents.items():
#             if key == val_tmp:
#                 path.append(key)
#                 if ( val is None ) or ( val == [None] ):
#                     break
                
#                 val_tmp = val[0] # беремо першого (поки що)

#         path.reverse()
#         paths_list.append(path)
    
#     return paths_list


# get dict value by its index
def get_value_from_dict(my_dict, index):
    return list( my_dict.values() )[index]


# get dict key by its index
def get_key_from_dict(my_dict, index):
    return list( my_dict.keys() )[index]


# get value from internal dict
def get_value_from_internal_dict(outer_dict, index_in, index_out):
    inner_dict = get_value_from_dict(outer_dict, index_out)
    if not inner_dict:   # if inner_dict not empty
        return list( inner_dict.values() )[index_in]
    else:
        return None
    

# get key from internal dict
def get_key_from_internal_dict(outer_dict, index_in, index_out):
    inner_dict = get_key_from_dict(outer_dict, index_out)
    if not inner_dict:   # if inner_dict not empty
        return list( inner_dict.keys() )[index_in]
    else:
        return None



# Eample:
# # A --5-- B --2-- C
#     graph_dict = {
#             'A': {'B': 5},
#             'B': {'A': 5, 'C':2},
#             'C': {'B': 2}
#         }
#     result = dijkstras_alg(graph_dict, 'A')
#     assert result == {'A': 0, 'B': 5, 'C': 7}


# # Dijkstra's algorithm ( for undirected weighted graphs ) with deque module
# def dijkstras_alg(graph_dict, start_vertex): #, distances):
#     count_infs = len( list( graph_dict.keys() ) )
#     distances = ['inf' for i in range(count_infs)]
#     distances[0] = 0  # [0] - це тіко якщо ми вибрали перший елемент ('A'). Для 'C', напр., це буде [2]
#     curr_vertex = start_vertex
#     heapq = [ (0, curr_vertex) ]
#     path = {curr_vertex: distances[0]}
    
#     if len(graph_dict) == 1:
#         return path
    
#     in_dict = get_value_from_dict(graph_dict, 0)   # value of key 'A'
#     if not in_dict:   # if in_dict not empty
#         distances.append( float('inf') )
#         path[get_key_from_dict(graph_dict, 0)] = distances[1]
#         return path
    
#     counter = 0
#     while heapq:
#         curr_distance = distances[counter]
#         heapq.pop((distances[counter], curr_vertex))

#         if curr_distance > distances[curr_vertex]:
#             continue # outdated entry ???

#         # Relax of neighbors u of curr_vertex
#         new_distance = curr_distance + weight( curr_vertex, neighbor)
#         if new_distance < distances[neighbor]:
#             # update distances[neighbor]
#             distances[neighbor] = new_distance
#             heapq.push(new_distance, neighbor)

#         counter += 1

#     # # distances.append( list( in_dict.values() )[0] )
#     # distances.append( get_value_from_dict(in_dict, 0) )
#     # path[get_key_from_dict(graph_dict, 1)] = distances[1]
    
#     return path
    


    # # curr_node = start_vertex
    # distance = [0, 'inf']
    # path = graph_dict
    # if distance[1] == 'inf'
    #     distance[1] = distance[0] + graph_dict['B']
    # print(f'distance == {distance}')
    # path['B'] = distance[1]


def dijkstras_alg(graph_dict, start_vertex): #, distances):
    pass