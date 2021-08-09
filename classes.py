import utils
import travel

import pyxel
import math
class Button:
    def __init__(self, text, x, y, color):
        self.text = text
        self.posx = x
        self.posy = y
        self.color = color
        
    def update(self):
        mouse_pos = [pyxel.mouse_x, pyxel.mouse_y]
        bpos = [self.posx, self.posy]
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and (math.dist(mouse_pos, bpos) < 15):
            return 1

    def draw(self):
        pyxel.circ(self.posx, self.posy, 15, self.color)
        pyxel.text(utils.x_fix(self.posx, self.text), self.posy, self.text, 7)

        
class Node:
    def __init__(self, key, x, y, col):
        self.key = key
        self.posx = x
        self.posy = y
        self.color = col

    def update(self, flag):
        mouse_pos = [pyxel.mouse_x, pyxel.mouse_y]
        node_pos = [self.posx, self.posy]

        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and (math.dist(mouse_pos, node_pos) < 6):
            
            if flag == 'DFS':
                aux = travel.user_dfs(self.key, utils.graph)
            elif flag == 'BFS':
                aux = travel.user_bfs(self.key, utils.graph)

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

    def draw(self, id):

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
        self.center = (utils.WIDTH/4)*3

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
        
        newy = 25+offset*layer
        newx = self.center - offset*self.layers[layer]/2 + it*offset

    
        self.tree_nodes.append(Tree_node(key, newx, newy, 11, layer, parent))
        self.layers[layer] += 1
        
    def draw(self):
        for node in self.tree_nodes:
            node.draw(0)

        for node in self.tree_nodes:
            node.draw(1)