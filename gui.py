import pygame
from cube import Cube

class Gui:
	size = (800, 600) # window size
	margin = 10 # distance between cube and side
	gridSize = 20 # size of grids
	blackGrids = 1 # number of grids occupied by black plastic borders
	colourGrids = 2 # number of grids occupied by coloured stickers
	colourMap = {
		-1: (0, 0, 0),       # black for plastic
		-2: (100, 100, 100),  # grey for borders
		Cube.u: (255, 255, 255),	# white
		Cube.d: (0, 255, 255),		# yellow
		Cube.f: (0, 255, 0),       	# green
		Cube.b: (0, 0, 255),		# blue
		Cube.r: (255, 0, 0),		# red
		Cube.l: (0, 127, 255)		# orange
	}
	edgeWidth = 2

	def __init__(self):
		self.screen = pygame.display.set_mode(Gui.size)

	def get_colour(self, face):
		return Gui.colourMap[face]

	def get_polygons(self, cubeData):
		sideGrids = Gui.colourGrids * 3 + Gui.blackGrids * 4
		polygons = []
		# black plastic
		polygons.append(
			(
				-1, 
				[
					(0, sideGrids), (0, sideGrids * 2), (sideGrids, sideGrids * 2),
					(sideGrids * 2, sideGrids), (sideGrids * 2, 0), (sideGrids, 0)
				]
			)
		)
		# grey borders
		polygons.append(
			(
				-2,
				[
					(0, sideGrids), (0, sideGrids * 2),
					(sideGrids, sideGrids * 2), (sideGrids, sideGrids)
				]
			)
		)
		polygons.append(
			(
				-2,
				[
					(0, sideGrids), (sideGrids, sideGrids),
					(sideGrids * 2, 0), (sideGrids, 0)
				]
			)
		)
		polygons.append(
			(
				-2,
				[
					(sideGrids, sideGrids), (sideGrids, sideGrids * 2),
					(sideGrids * 2, sideGrids), (sideGrids * 2, 0)
				]
			)
		)
		# front face
		for y in range(3):
			for x in range(3):
				colour = cubeData[Cube.f][y][x]
				points = [
					(Gui.blackGrids * (x + 1) + Gui.colourGrids * x,
					sideGrids + Gui.blackGrids * (y + 1) + Gui.colourGrids * y),
					((Gui.blackGrids + Gui.colourGrids) * (x + 1),
					sideGrids + Gui.blackGrids * (y + 1) + Gui.colourGrids * y),
					((Gui.blackGrids + Gui.colourGrids) * (x + 1),
					sideGrids + (Gui.blackGrids + Gui.colourGrids)* (y + 1)),
					(Gui.blackGrids * (x + 1) + Gui.colourGrids * x,
					sideGrids + (Gui.blackGrids + Gui.colourGrids)* (y + 1))
				]
				polygons.append((colour, points))
		# up face
		for y in range(3):
			for x in range(3):
				colour = cubeData[Cube.u][y][x]
				points = [
					(Gui.blackGrids * (x + 1) + Gui.colourGrids * x,
					Gui.blackGrids * (y + 1) + Gui.colourGrids * y),
					((Gui.blackGrids + Gui.colourGrids) * (x + 1),
					Gui.blackGrids * (y + 1) + Gui.colourGrids * y),
					((Gui.blackGrids + Gui.colourGrids) * (x + 1),
					(Gui.blackGrids + Gui.colourGrids)* (y + 1)),
					(Gui.blackGrids * (x + 1) + Gui.colourGrids * x,
					(Gui.blackGrids + Gui.colourGrids)* (y + 1))
				]
				skewedPoints = [(sideGrids + point[0] - point[1], point[1])
										for point in points]
				polygons.append((colour, skewedPoints))
		# right face
		for y in range(3):
			for x in range(3):
				colour = cubeData[Cube.r][y][x]
				points = [
					(Gui.blackGrids * (x + 1) + Gui.colourGrids * x,
					Gui.blackGrids * (y + 1) + Gui.colourGrids * y),
					((Gui.blackGrids + Gui.colourGrids) * (x + 1),
					Gui.blackGrids * (y + 1) + Gui.colourGrids * y),
					((Gui.blackGrids + Gui.colourGrids) * (x + 1),
					(Gui.blackGrids + Gui.colourGrids)* (y + 1)),
					(Gui.blackGrids * (x + 1) + Gui.colourGrids * x,
					(Gui.blackGrids + Gui.colourGrids)* (y + 1))
				]
				skewedPoints = [(sideGrids + point[0], sideGrids + point[1] - point[0])
										for point in points]
				polygons.append((colour, skewedPoints))
		return polygons

	def draw(self, cubeData):
		polygons = self.get_polygons(cubeData)
		self.screen.fill((255, 255, 255)) # white background
		for polygon in polygons:
			points = [(i[0] * Gui.gridSize + Gui.margin, i[1] * Gui.gridSize + Gui.margin)
					for i in polygon[1]]
			width = Gui.edgeWidth if polygon[0] == -2 else 0
			colour = self.get_colour(polygon[0])
			pygame.draw.polygon(self.screen, colour, points, width)
		pygame.display.flip()