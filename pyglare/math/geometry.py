import math

class Vector:
	
	def __init__(self,x,y,z):
		self.x = x
		self.y = y
		self.z = z
	
	def length(self):
		return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
	
	def normalize(self):
		return self / self.length()
	
	def __add__(self,vec):
		return Vector(self.x + vec.x,self.y + vec.y,self.z + vec.z)
		
	def __sub__(self,vec):
		return Vector(self.x - vec.x,self.y - vec.y,self.z - vec.z)
	
	def __neg__(self):
		return Vector(-self.x,-self.y,-self.z)
	
	def __mul__(self,num):
		return Vector(self.x * num,self.y * num,self.z * num)
	
	def __truediv__(self,num):
		return Vector(self.x / num,self.y / num,self.z / num)
		
	def dot(a,b):
		return a.x*b.x + a.y*b.y + a.z*b.z
	
	def cross(a,b):
		return Vector(a.y*b.z - a.z*b.y,
						a.z*b.x - a.x*b.z,
						a.x*b.y - a.y*b.x)
						
	def reflect(self,vec):
		mirror=self * Vector.dot(self,vec)/Vector.dot(self,self)
		return (mirror*2-vec).normalize()
	
	
class Ray:
	
	def __init__(self,position,direction):
		self.position = position
		self.direction = direction

class Plane:
	
	def __init__(self,normal,intercept):
		self.normal = normal
		self.intercept = intercept
	
	def intersection(self,ray):
		div=Vector.dot(ray.direction,self.normal)
		if div==0:	# Plane and ray are parallel!
			return None
		t = -(Vector.dot(ray.position,self.normal)+self.intercept)/div
		if t>0:
			return t
		else:
			return None
		
class Sphere:
	
	def __init__(self,position,radius):
		self.position = position
		self.radius = radius
	
	def intersection(self,ray):
		tca=Vector.dot(self.position-ray.position,ray.direction)
		if tca<0:
			return None
		d2=Vector.dot(self.position-ray.position,self.position-ray.position)-tca*tca
		if d2 > self.radius ** 2:
			return None
		thc=math.sqrt(self.radius ** 2 - d2)
		ret=min(tca-thc,tca+thc)
		if ret<0:
			return None
		else:
			return ret

class Triangle:
	
	def __init__(self,a,b,c):
		self.a = a
		self.b = b
		self.c = c
	
	
	
