class Cube:
	u = 0
	l = 1
	f = 2
	r = 3
	b = 4
	d = 5

	def __init__(self):
		self.data = [[[k for i in range(3)] for j in range(3)] for k in range(6)]
		"""
		[[0,0,0],
		[0,0,0],
		[0,0,0]],
[[1,1,1]]  [2,2,2]
[1,1,1]    [2,2,2]
[1,1,1]    [2,2,2]




		"""

	def printNet(self):
		for i in self.data[0]:
			print("      ", i)
		for i in range(3):
			for j in range(4):
				print(self.data[j+1][i], end="  ")
			print()
		for i in self.data[5]:
			print("      ", i)


	def turnFace(self, face):# face = "R"
		self.data[3] = [[1,2,3],[4,5,6],[7,8,9]]
		self.data[0] = [[0,0,"c"],[0,0,"b"],[0,0,"a"]]
		self.data[4] = [["d",0,0],["e",0,0],["f",0,0]]
		self.data[5] = [[0,0,"i"],[0,0,"h"],[0,0,"g"]]
		self.data[2] = [[0,0,"l"],[0,0,"k"],[0,0,"j"]]
		self.printNet()

		if face == self.r:
			self.data[3][0][2], self.data[3][1][2], self.data[3][2][2], self.data[3][0][1], self.data[3][2][1], self.data[3][0][0], self.data[3][1][0], self.data[3][2][0] = self.data[3][0][0], self.data[3][0][1], self.data[3][0][2], self.data[3][1][0], self.data[3][1][2], self.data[3][2][0], self.data[3][2][1], self.data[3][2][2]
			self.data[0][2][2], self.data[0][1][2], self.data[0][0][2], self.data[4][0][0], self.data[4][1][0], self.data[4][2][0], self.data[5][2][2], self.data[5][1][2], self.data[5][0][2], self.data[2][2][2], self.data[2][1][2], self.data[2][0][2] = self.data[2][2][2], self.data[2][1][2], self.data[2][0][2], self.data[0][2][2], self.data[0][1][2], self.data[0][0][2], self.data[4][0][0], self.data[4][1][0], self.data[4][2][0], self.data[5][2][2], self.data[5][1][2], self.data[5][0][2]
			self.printNet()

		


cube = Cube()
cube.turnFace(cube.r)

