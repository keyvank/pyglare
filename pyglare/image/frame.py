class Frame:
	
	def __init__(self,width,height,color):
		self.width = width
		self.height = height
		self.data = []
		for h in range(height):
			row = []
			for w in range(width):
				row.append(color)
			self.data.append(row)
	
	def clear(self,color):
		for h in range(self.height):
			for w in range(self.width):
				self.data[h][w] = color
