import math
import pyxel
import random

graph = {}

WIDTH = 256
HEIGTH = 196

def generate_graph(n: int):
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

graph = generate_graph(random.randrange(6, 7))

visited = []

def dfs(node):
    if node not in visited:
        print(node)
        visited.append(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                dfs(neighbour)


current_node = '-1'
stack_dfs = []
mistake = 0

def user_dfs(node):
    global current_node
    global stack_dfs
    global mistake
    
    if node in visited:
        return 1
        
    if current_node == '-1':
        current_node = node
        visited.append(node)
        stack_dfs.append(node)
        return 0
    else:
        if node in graph[current_node] and node not in visited:
            current_node = node
            visited.append(node)
            stack_dfs.append(node)
            return 0
        else:
            flag = 0
            stack_bkp = stack_dfs.copy()

            while flag == 0:
                for n in graph[current_node]:
                    if n not in visited and n != node:
                        flag = 1
                    elif n not in visited and n == node:
                        current_node = node
                        visited.append(node)
                        stack_dfs.append(node)
                        flag = 2
                        break
                if flag == 2:
                    return 0
                if flag == 1:
                    mistake += 1
                    stack_dfs = stack_bkp.copy()
                    if stack_dfs != []:
                        current_node = stack_dfs[-1]
                    return 1
                else:
                    stack_dfs.pop()
                    if stack_dfs != []:
                        current_node = stack_dfs[-1]
                 
class Node:
    def __init__(self, key, x, y, col):
        # self.neighbours = lst
        self.posx = x
        self.posy = y
        self.key = key
        self.color = col


    def update(self):
        mouse_pos = [pyxel.mouse_x, pyxel.mouse_y]
        node_pos = [self.posx, self.posy]

        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and (math.dist(mouse_pos, node_pos) < 6):
            # print(f"Clicou no nózin = {self.key} 😎")
            aux = user_dfs(self.key)
            if aux == 0:
                self.color = ((self.color-5)%2)+6
        
    def draw(self):
        pyxel.circ(self.posx, self.posy, 5, self.color)
        pyxel.text(self.posx, self.posy, self.key, 8)

class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGTH, caption="My traversal Coach")
        pyxel.mouse(True)
        
        self.nodes = []
        num_nodes = graph.__len__()
        for i in range(0, num_nodes):
            x = pyxel.width/2+math.sin(math.radians((360/num_nodes)*i))*80
            y = pyxel.height/2+math.cos(math.radians((360/num_nodes)*i))*50

            self.nodes.append(Node(str(i), x, y, 7))
            
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        for node in self.nodes:
            node.update()


    def draw(self):
        
        pyxel.cls(0)
       
        
        for node in self.nodes:

            for neighbours in graph[node.key]:
                pyxel.line(node.posx, node.posy, self.nodes[int(neighbours)].posx, self.nodes[int(neighbours)].posy, 10)


        for node in self.nodes:
            node.draw()

        pyxel.text(WIDTH-50, 10, f'MISTAKES: {mistake}', 8)



App()
