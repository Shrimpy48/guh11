from gui import Gui
from cube import Cube
from time import sleep

cube = Cube()
gui = Gui()
while True:
	event = gui.handle()
	if event == -1:
		break
	else:
		gui.draw(cube.data)