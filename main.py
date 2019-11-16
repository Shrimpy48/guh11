from gui import Gui
from cube import Cube
from time import sleep

cube = Cube()
gui = Gui()
gui.draw(cube.data)
cube.turn_layer(cube.f)
sleep(1)
gui.draw(cube.data)
input()