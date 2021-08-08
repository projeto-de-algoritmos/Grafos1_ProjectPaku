import math
import pyxel

graph = {
  '0' : ['1'],
  '1' : ['0', '2','5'],
  '2' : ['1', '3', '5'],
  '3' : ['2', '4'],
  '4' : ['3', '5', '6'],
  '5' : ['1', '4', '2'],
  '6' : ['4']
}

WIDTH = 256
HEIGTH = 196

class Node:
    def __init__(self, key, x, y, col):
        self.posx = x
        self.posy = y
        self.key = key
        self.color = col


    def update(self):
        mouse_pos = [pyxel.mouse_x, pyxel.mouse_y]
        node_pos = [self.posx, self.posy]

        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and (math.dist(mouse_pos, node_pos) < 6):
            print(f"Clicou no nózinho = {self.key} 😎")
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

App()
