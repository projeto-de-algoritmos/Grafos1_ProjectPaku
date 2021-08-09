import travel
import utils
import classes

import math
import pyxel
import random

utils.graph = utils.generate_graph(random.randrange(4, 6))
# print(utils.graph)
class App:
    def __init__(self):
        pyxel.init(utils.WIDTH, utils.HEIGHT, caption="My Traversal Coach")
        pyxel.mouse(True)
        self.travel = 'DFS'
        self.btn_traveld = classes.Button('DFS', utils.WIDTH/2 -50, utils.HEIGHT/2+20, 3)
        self.btn_travelb = classes.Button('BFS', utils.WIDTH/2 +50, utils.HEIGHT/2+20, 3)

        self.done = 0
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

        if(utils.visited.__len__() != utils.graph.__len__()) and self.done == 0:
            if pyxel.frame_count % 24 == 0:
                self.timer += 1
        else:
            if self.done == 0:
                self.done = 1
            

        if utils.state == 0:
            if self.btn_travelb.update() == 1:
                self.travel = "BFS"
                utils.state = 1
            if self.btn_traveld.update() == 1:
                self.travel = "DFS"
                utils.state = 1
        elif utils.state == 1:

            if self.done == 1:
                if pyxel.btnp(pyxel.KEY_R):
                    utils.state = 0
                    utils.mistakes = 0
                    utils.visited = []
                    utils.graph = utils.generate_graph(random.randrange(4, 6))

                    self.done = 0
                    self.timer = 0
                    self.nodes = []
                    num_nodes = utils.graph.__len__()
                    for i in range(0, num_nodes):
                        x = pyxel.width/4+math.sin(math.radians((360/num_nodes)*i))*50
                        y = pyxel.height/2+math.cos(math.radians((360/num_nodes)*i))*40

                        self.nodes.append(classes.Node(str(i), x, y, 7))

                    #BFS vars
                    travel.cn_iterator = 0 # cn = current node
                    travel.cn_list = []
                    travel.cn_layers = []
                    travel.queue_bfs = []

                    # DFS vars
                    travel.stack_dfs = []
                    travel.current_node = '-1'


                    self.tree.tree_nodes = []
                    self.tree.layers = []

            for node in self.nodes:
                if node.update(self.travel) == 1:
                    # TRATA APENAS A ARVORE BFS
                    if self.travel == 'BFS':
                        if travel.cn_layers.__len__() == 1 :
                            parent = None
                            node_layer = travel.cn_layers[travel.cn_iterator]
                        else:
                            node_layer = travel.cn_layers[travel.cn_iterator]+1
                            for tnode in self.tree.tree_nodes:
                                if tnode.key == travel.cn_list[travel.cn_iterator]:
                                    parent = tnode
                                    
                        self.tree.add_node(node.key, node_layer, parent)
                    elif self.travel == 'DFS':
                        # TRATA APENAS A ARVORE DFS ↓
                        key = travel.stack_dfs[-1]
                        layer = travel.stack_dfs.__len__() - 1
                        if layer == 0:
                            parent = None
                        else:
                            for node in self.tree.tree_nodes:
                                if node.key == travel.stack_dfs[layer-1]:
                                    parent = node
                        self.tree.add_node(key, layer, parent)

    def draw(self):
        pyxel.cls(0)

        if utils.state == 0:           
            pyxel.text(utils.x_fix(utils.WIDTH/2, "MY TRAVERSAL COACH"), utils.HEIGHT/2-50, "MY TRAVERSAL COACH", 7)

            self.btn_traveld.draw()
            self.btn_travelb.draw()

        elif utils.state == 1:
            pyxel.line(utils.WIDTH/2 , 0, utils.WIDTH/2, utils.HEIGHT, 5)
            pyxel.text(3, 3, "GRAFO", 10)
            pyxel.text(utils.WIDTH/2+5, 3, "ARVORE", 10)
            pyxel.text(3, utils.HEIGHT-10, f'ERROS: {utils.mistakes}', 7)
            pyxel.text(utils.WIDTH/2-40, utils.HEIGHT-10, f'TEMPO: {self.timer}', 7)
            
            #color = 0
            for node in self.nodes:
                for neighbours in utils.graph[node.key]:
                    pyxel.line(node.posx, node.posy, self.nodes[int(neighbours)].posx, self.nodes[int(neighbours)].posy, 8)
                #color+=1
            for node in self.nodes:
                node.draw()

            self.tree.draw()

            if self.done == 1:
                txt = """PRESSIONE A TECLA "R" PARA JOGAR NOVAMENTE"""
                # pyxel.rect(utils.x_fix(utils.WIDTH/2, txt), utils.HEIGHT/2-50, , )

                outline_col = 7
                pyxel.text(utils.x_fix(utils.WIDTH/2, txt)-1, utils.HEIGHT/2+70-1, txt, outline_col)
                pyxel.text(utils.x_fix(utils.WIDTH/2, txt)+1, utils.HEIGHT/2+70+1, txt, outline_col)
                pyxel.text(utils.x_fix(utils.WIDTH/2, txt)-1, utils.HEIGHT/2+70+1, txt, outline_col)
                pyxel.text(utils.x_fix(utils.WIDTH/2, txt)+1, utils.HEIGHT/2+70-1, txt, outline_col)
                pyxel.text(utils.x_fix(utils.WIDTH/2, txt), utils.HEIGHT/2+70-1, txt, outline_col)
                pyxel.text(utils.x_fix(utils.WIDTH/2, txt), utils.HEIGHT/2+70+1, txt, outline_col)
                pyxel.text(utils.x_fix(utils.WIDTH/2, txt)-1, utils.HEIGHT/2+70, txt, outline_col)
                pyxel.text(utils.x_fix(utils.WIDTH/2, txt)+1, utils.HEIGHT/2+70, txt, outline_col)
                pyxel.text(utils.x_fix(utils.WIDTH/2, txt), utils.HEIGHT/2+70, txt, 8)
# importante  
App()