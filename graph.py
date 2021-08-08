import math
import pyxel
import random

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

graph = {}
graph = generate_graph(random.randrange(5, 6))

visited = []
stack_dfs = []
queue_bfs = []
current_node = '-1'
mistake = 0

def user_bfs(node):
    global queue_bfs
    global visited
    global mistake

    if node in visited:
        return 1

    if visited == []:
        visited.append(node)
        queue_bfs.append(graph[node].copy())
        return 0
    else:

        clean = True
        while clean:
            clean = False
            for i in queue_bfs[0]:
                if i in visited:
                    queue_bfs[0].remove(i)
                    clean = True
            if queue_bfs[0] == []:
                queue_bfs.pop(0)
                clean = True

        ############## 
        for i in queue_bfs[0]:
            if i in visited:
                print(f'{i} ja foi visitado')
        ##############

        if node in queue_bfs[0]:
            visited.append(node)
            queue_bfs.append(graph[node].copy())
            queue_bfs[0].remove(node)
            # print(f'# {queue_bfs}')
            return 0 
        else:
            mistake += 1
            # print(queue_bfs)
            return 1
        

def user_dfs(node):
    global stack_dfs
    global visited
    global current_node
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
        self.key = key
        self.posx = x
        self.posy = y
        self.color = col

    def update(self):
        mouse_pos = [pyxel.mouse_x, pyxel.mouse_y]
        node_pos = [self.posx, self.posy]

        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and (math.dist(mouse_pos, node_pos) < 6):
            # print(f"Clicou no nózin = {self.key} 😎")
            # aux = user_dfs(self.key)
            aux = user_bfs(self.key)
            if aux == 0:
                self.color = ((self.color-5)%2)+6
                return 1

        return 0
        
    def draw(self):
        pyxel.circ(self.posx, self.posy, 5, self.color)
        pyxel.text(self.posx, self.posy, self.key, 8)

class Tree_node(Node):
    def __init__(self, key, x, y, col, layer, parent: Node = None):
        super().__init__(key, x, y, col)
        self.key = key
        self.posx = x
        self.posy = y
        self.color = col
        self.layer = layer
        self.parent = parent
        self.show = True

    def draw(self, id):

        if self.show:
            if id == 0:
                if self.parent != None:
                    pyxel.line(self.posx, self.posy, self.parent.posx, self.parent.posy, 10)

            elif id == 1:
                pyxel.circ(self.posx, self.posy, 5, self.color)
                pyxel.text(self.posx, self.posy, self.key, 8)

class Tree:
    def __init__(self):
        self.tree_nodes = []
        self.layers = []
        self.center = (WIDTH/4)*3

    def add_node(self, key, layer, parent):
        offset = 20
        it = 0
        
        if self.layers.__len__() <= layer :
            self.layers.append(0)

        for node in self.tree_nodes:
            if node.layer == layer:
                newx = self.center - offset*self.layers[layer]/2 + it*offset
                node.posx = newx
                it += 1
        
        newy = 20+offset*layer
        newx = self.center - offset*self.layers[layer]/2 + it*offset

        self.tree_nodes.append(Tree_node(key, newx, newy, 13, layer, parent))

        self.layers[layer] += 1
        
    def draw(self):
        for node in self.tree_nodes:
            node.draw(0)

        for node in self.tree_nodes:
            node.draw(1)

class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGTH, caption="My Traversal Coach")
        pyxel.mouse(True)
        
        self.nodes = []
        self.tree = Tree()
        num_nodes = graph.__len__()
        for i in range(0, num_nodes):
            x = pyxel.width/4+math.sin(math.radians((360/num_nodes)*i))*40
            y = pyxel.height/2+math.cos(math.radians((360/num_nodes)*i))*25

            self.nodes.append(Node(str(i), x, y, 7))
            
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        for node in self.nodes:
            if node.update() == 1:
                ...
                # TRATA APENAS A ARVORE DFS ↓
                # key = stack_dfs[-1]
                # layer = stack_dfs.__len__() - 1
                # if layer == 0:
                #     parent = None
                # else:
                #     for node in self.tree.tree_nodes:
                #         if node.key == stack_dfs[layer-1]:
                #             parent = node
                # self.tree.add_node(key, layer, parent)

    def draw(self):
        pyxel.cls(0)
        pyxel.line(WIDTH/2 , 0, WIDTH/2, HEIGTH, 5)
        pyxel.text(3, 3, "GRAFO", 8)
        pyxel.text(WIDTH/2+5, 3, "ARVORE", 8)
        pyxel.text(3, HEIGTH-10, f'MISTAKES: {mistake}', 8)
        
        for node in self.nodes:
            for neighbours in graph[node.key]:
                pyxel.line(node.posx, node.posy, self.nodes[int(neighbours)].posx, self.nodes[int(neighbours)].posy, 10)

        for node in self.nodes:
            node.draw()

        self.tree.draw()

App()