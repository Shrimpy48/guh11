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

	def turnFace(self, face):# face = "R"
		print(self.data)
		if face == self.r:
			self.data[3][0][0], self.data[3][0][1] = self.data[]



	
