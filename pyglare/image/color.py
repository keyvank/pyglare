class Color:
	
	def __init__(self,r,g,b):
		self.r = r
		self.g = g
		self.b = b
	
	def get_bytes(self):
		return bytes([int(min(self.r*255,255)),int(min(self.g*255,255)),int(min(self.b*255,255))])
	
	def __add__(self,col):
		return Color(self.r+col.r,self.g+col.g,self.b+col.b)
		
	def __sub__(self,col):
		return Color(self.r-col.r,self.g-col.g,self.b-col.b)
	
	def __mul__(self,other):
		if isinstance(other,Color):
			return Color(self.r*other.r,self.g*other.g,self.b*other.b)
		else:
			return Color(self.r*other,self.g*other,self.b*other)

	def __truediv__(self,other):
		if isinstance(other,Color):
			return Color(self.r/other.r,self.g/other.g,self.b/other.b)
		else:
			return Color(self.r/other,self.g/other,self.b/other)
	
	def from_rgb(r,g,b):
		return Color(r/255,g/255,b/255)

BLACK = Color(0,0,0)
WHITE = Color(1,1,1)
RED = Color(1,0,0)
GREEN = Color(0,1,0)
BLUE = Color(0,0,1)
YELLOW = Color(1,1,0)
MAGENTA = Color(1,0,1)
CYAN = Color(0,1,1)
