import utils

# BFS vars
cn_iterator = 0 # cn = current node
cn_list = []
cn_layers = []
queue_bfs = []

# DFS vars
stack_dfs = []
current_node = '-1'

def user_bfs(node, graph):
    global queue_bfs
    global cn_iterator
    global cn_layers
    global cn_list
    
    if node in utils.visited:
        return 1

    if utils.visited == []:
        utils.visited.append(node)
        queue_bfs.append(graph[node].copy())
        cn_list.append(node)
        cn_layers.append(cn_iterator)
        return 0
    else:
        clean = True
        while clean:
            clean = False
            for i in queue_bfs[0]:
                if i in utils.visited:
                    queue_bfs[0].remove(i)
                    clean = True
            if queue_bfs[0] == []:
                queue_bfs.pop(0)
                
                cn_iterator += 1
                clean = True

      
        if node in queue_bfs[0]:
            utils.visited.append(node)
            queue_bfs.append(graph[node].copy())
            queue_bfs[0].remove(node)
            cn_list.append(node)
            cn_layers.append(cn_layers[cn_iterator]+1)
            return 0 
        else:
            utils.mistakes += 1
            return 1

def user_dfs(node, graph):
    global stack_dfs
    global current_node
    
    if node in utils.visited:
        return 1
        
    if current_node == '-1':
        current_node = node
        utils.visited.append(node)
        stack_dfs.append(node)
        return 0
    else:
        if node in graph[current_node] and node not in utils.visited:
            current_node = node
            utils.visited.append(node)
            stack_dfs.append(node)
            return 0
        else:
            flag = 0
            stack_bkp = stack_dfs.copy()

            while flag == 0:
                for n in graph[current_node]:
                    if n not in utils.visited and n != node:
                        flag = 1
                    elif n not in utils.visited and n == node:
                        current_node = node
                        utils.visited.append(node)
                        stack_dfs.append(node)
                        flag = 2
                        break

                if flag == 2:
                    return 0
                if flag == 1:
                    utils.mistakes += 1
                    stack_dfs = stack_bkp.copy()
                    if stack_dfs != []:
                        current_node = stack_dfs[-1]
                    return 1
                else:
                    stack_dfs.pop()
                    if stack_dfs != []:
                        current_node = stack_dfs[-1]

# visited = [] 
# queue = []

# def dfs(node):
#     if node not in visited:
#         print(node)
#         visited.append(node)
#         for neighbour in graph[node]:
#             if neighbour not in visited:
#                 dfs(neighbour)

# def bfs(node):
#   visited.append(node)
#   queue.append(node)

#   while queue:
#     s = queue.pop(0) 
#     print (s) 

#     for neighbour in graph[s]:
#       if neighbour not in visited:
#         visited.append(neighbour)
#         queue.append(neighbour)

# dfs('0')
# bfs('0')
# print("")