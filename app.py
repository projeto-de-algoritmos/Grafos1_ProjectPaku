import travel
import utils
import classes

import math
import pyxel
import random

utils.graph = utils.generate_graph(random.randrange(4, 6))

class App:
    def __init__(self):
        pyxel.init(utils.WIDTH, utils.HEIGTH, caption="My Traversal Coach")
        pyxel.mouse(True)
        self.timer = 0
        self.nodes = []
        self.tree = classes.Tree()
        num_nodes = utils.graph.__len__()
        for i in range(0, num_nodes):
            x = pyxel.width/4+math.sin(math.radians((360/num_nodes)*i))*50
            y = pyxel.height/2+math.cos(math.radians((360/num_nodes)*i))*40

            self.nodes.append(classes.Node(str(i), x, y, 7))
            
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if(utils.visited.__len__() != utils.graph.__len__()):
            if pyxel.frame_count % 24 == 0:
                self.timer += 1

        for node in self.nodes:
            if node.update() == 1:
                # TRATA APENAS A ARVORE BFS

                if travel.cn_layers.__len__() == 1 :
                    parent = None
                    node_layer = travel.cn_layers[travel.cn_iterator]
                else:
                    node_layer = travel.cn_layers[travel.cn_iterator]+1
                    for tnode in self.tree.tree_nodes:
                        if tnode.key == travel.cn_list[travel.cn_iterator]:
                            parent = tnode
                            
                self.tree.add_node(node.key, node_layer, parent)
                
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
        global visited
        pyxel.cls(0)
        pyxel.line(utils.WIDTH/2 , 0, utils.WIDTH/2, utils.HEIGTH, 5)
        pyxel.text(3, 3, "GRAFO", 10)
        pyxel.text(utils.WIDTH/2+5, 3, "ARVORE", 10)
        pyxel.text(3, utils.HEIGTH-10, f'ERROS: {utils.mistakes}', 7)
        pyxel.text(utils.WIDTH/2-40, utils.HEIGTH-10, f'TEMPO: {self.timer}', 7)

        color = 0
        for node in self.nodes:
            for neighbours in utils.graph[node.key]:
                pyxel.line(node.posx, node.posy, self.nodes[int(neighbours)].posx, self.nodes[int(neighbours)].posy, color)
            color+=1
        for node in self.nodes:
            node.draw()

        self.tree.draw()

App()