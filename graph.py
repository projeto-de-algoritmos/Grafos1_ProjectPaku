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

class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGTH, caption="Hello Pyxel")
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        
        pyxel.cls(0)

        num_nodes = graph.__len__()

        for i in range(0, num_nodes):
            x = pyxel.width/2+math.sin(math.radians((360/num_nodes)*i))*80
            y = pyxel.height/2+math.cos(math.radians((360/num_nodes)*i))*50

            pyxel.circ(x, y, 5, 7)
            pyxel.text(x, y, str(i), 8)

App()