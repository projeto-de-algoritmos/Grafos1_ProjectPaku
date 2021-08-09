import travel
import utils
import classes

import math
import pyxel
import random

class App:
    def __init__(self):
        pyxel.init(utils.WIDTH, utils.HEIGHT, caption="My Traversal Coach")
        pyxel.mouse(True)
        self.travel = 'DFS'
        self.graph_len = -1
        self.btn_traveld = classes.Button('DFS', utils.WIDTH/2 -50, utils.HEIGHT/2+40, 3)
        self.btn_travelb = classes.Button('BFS', utils.WIDTH/2 +50, utils.HEIGHT/2+40, 3)

        self.done = 0
        self.timer = 0
        
        self.nodes = []
        self.tree = classes.Tree()
       
            
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if(utils.visited.__len__() != utils.graph.__len__()) and self.done == 0:
            if pyxel.frame_count % 30 == 0:
                self.timer += 1
        else:
            if self.done == 0:
                self.done = 1
            

        if utils.state == 0:
            if pyxel.btnp(pyxel.KEY_RIGHT):
                if self.graph_len == -1:
                    self.graph_len = 12
                elif self.graph_len < 12:
                    self.graph_len +=1
                
            if pyxel.btnp(pyxel.KEY_LEFT):
                if self.graph_len == -1:
                    self.graph_len = 4
                elif self.graph_len > 4:
                    self.graph_len -=1
            if pyxel.btnp(pyxel.KEY_SPACE):
                    self.graph_len = -1
            if self.btn_travelb.update() == 1:
                if self.graph_len == -1:
                    utils.graph = utils.generate_graph(random.randrange(4, 12))
                else:
                    utils.graph = utils.generate_graph(self.graph_len)
                self.nodes = []
                num_nodes = utils.graph.__len__()
                for i in range(0, num_nodes):
                    x = pyxel.width/4+math.sin(math.radians((360/num_nodes)*i))*50
                    y = pyxel.height/2+math.cos(math.radians((360/num_nodes)*i))*40

                    self.nodes.append(classes.Node(str(i), x, y, 7))
                self.travel = "BFS"
                self.done = 0
                utils.state = 1
            if self.btn_traveld.update() == 1:
                if self.graph_len == -1:
                    utils.graph = utils.generate_graph(random.randrange(4, 12))
                else:
                    utils.graph = utils.generate_graph(self.graph_len)
                self.nodes = []
                num_nodes = utils.graph.__len__()
                for i in range(0, num_nodes):
                    x = pyxel.width/4+math.sin(math.radians((360/num_nodes)*i))*50
                    y = pyxel.height/2+math.cos(math.radians((360/num_nodes)*i))*40

                    self.nodes.append(classes.Node(str(i), x, y, 7))
                self.travel = "DFS"
                self.done = 0
                utils.state = 1
        elif utils.state == 1:

            if pyxel.btnp(pyxel.KEY_R):
                utils.state = 0
                utils.mistakes = 0
                utils.visited = []

                self.done = 0
                self.timer = 0
                

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
            pyxel.text(utils.x_fix(utils.WIDTH/2, "MY TRAVERSAL COACH"), utils.HEIGHT/2-70, "MY TRAVERSAL COACH", 7)
            ap2 = "PRESSIONE ESPACO PARA UMA QUANTIDADE ALEATORIA DE NOS"
            ap = "PRESIONE <- OU -> PARA ALTERAR A QUANTIDADE DE NOS"
            pyxel.text(utils.x_fix(utils.WIDTH/2, ap), utils.HEIGHT/2-30, ap, 7)
            pyxel.text(utils.x_fix(utils.WIDTH/2, ap2), utils.HEIGHT/2-15, ap2, 7)
            if self.graph_len == -1:
                ap3 = f"<- ? ->"
            else:
                ap3 = f"<- {self.graph_len} ->"
            pyxel.text(utils.x_fix(utils.WIDTH/2, "<- XX ->"), utils.HEIGHT/2+10, ap3, 7)

            self.btn_traveld.draw()
            self.btn_travelb.draw()

        elif utils.state == 1:
            pyxel.line(utils.WIDTH/2 , 15, utils.WIDTH/2, utils.HEIGHT, 11)
            pyxel.text(3, 3, "GRAFO", 10)
            if self.travel == "DFS":
                pyxel.text(utils.x_fix(utils.WIDTH/2, "DEPTH-FIRST SEARCH"), 3, "DEPTH-FIRST SEARCH", 11)
            else:
                pyxel.text(utils.x_fix(utils.WIDTH/2, "BREADTH-FIRST SEARCH"), 3, "BREADTH-FIRST SEARCH", 11)
            pyxel.text(utils.WIDTH - 30, 3, "ARVORE", 10)
            pyxel.text(3, utils.HEIGHT-10, f'ERROS: {utils.mistakes}', 7)
            pyxel.text(utils.WIDTH/2-50, utils.HEIGHT-10, f'TEMPO: {(self.timer//60):02d}:{(self.timer%60):02d} ', 7)
            
            for node in self.nodes:
                for neighbours in utils.graph[node.key]:
                    pyxel.line(node.posx, node.posy, self.nodes[int(neighbours)].posx, self.nodes[int(neighbours)].posy, 8)
            for node in self.nodes:
                node.draw()

            self.tree.draw()

            if self.done == 1:
                txt = """PRESSIONE A TECLA "R" PARA JOGAR NOVAMENTE"""

                if utils.mistakes == 0:
                    msg = "Parabens! voce concluiu a travessia sem errar!"
                elif utils.mistakes < 5:
                    msg = "Bem Jogado!"
                else:
                    msg = "Voce precisa treinar mais!"
                
                pyxel.rect(utils.WIDTH/2-1, utils.HEIGHT/2+58, 3, 21, 0)
                pyxel.text(utils.x_fix(utils.WIDTH/2, msg), utils.HEIGHT/2+60, msg, 7)

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

App()