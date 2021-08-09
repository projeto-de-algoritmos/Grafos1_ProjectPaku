import random

WIDTH = 256
HEIGTH = 196
mistakes = 0
visited = []
graph = {}

def generate_graph(n: int):
    graph = {}
    lst = []
    for i in range(0, n):
        lst.append([])

    for i in range(0, n):
        num = i
        while num == i or str(num) in lst[i]:
            num = random.randrange(0,n)

        lst[i].append(str(num))
        lst[num].append(str(i)) 

    for i in range(0, n):
        graph.update({str(i): lst[i]})

    return graph