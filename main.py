from gui import Gui
from cube import Cube
from time import sleep

cube = Cube()
gui = Gui()
while True:
    action = gui.handle()
    if action == -1:
        break
    elif action == 1:
    	gui.draw(cube.data)
    	cube.scramble()
    else:
        gui.draw(cube.data)
        if action is not None:
            cube.parse_moves(action)
        # sleep(0.05)
        # gui.draw(cube.data)