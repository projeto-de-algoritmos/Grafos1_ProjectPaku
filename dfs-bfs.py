graph = {
  '0' : ['1'],
  '1' : ['0', '2','5'],
  '2' : ['1', '3', '5'],
  '3' : ['2', '4'],
  '4' : ['3', '5', '6'],
  '5' : ['1', '4', '2'],
  '6' : ['4']
}
visited = [] 
queue = []

def dfs(node):
    if node not in visited:
        print(node)
        visited.append(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                dfs(neighbour)

def bfs(node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s) 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

dfs('0')
# bfs('0')
# print("")