from gui import Gui
from cube import Cube
from time import sleep

cube = Cube()
gui = Gui()
while True:
	action = gui.handle()
	if action == -1:
		break
	else:
		gui.draw(cube.data)
		#cube.parse_moves(action)
		sleep(0.05)
		gui.draw(cube.data)