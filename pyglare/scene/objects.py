from ..math import geometry as geo
from ..image.color import Color
import math

class Material:
	
	def __init__(self,color,diffuse_rate,specular_rate,specular_exponent,reflection_rate):
		self.color = color
		self.diffuse_rate = diffuse_rate
		self.specular_rate = specular_rate
		self.specular_exponent = specular_exponent
		self.reflection_rate = reflection_rate

class Object:
	
	def __init__(self,material):
		self.material=material
	
	def intersection(self,ray):
		'''Considering intersection point is: landa * ray, returns landa if there is intersection or None'''
		pass
	
	def normal_at(self,position):
		'''Returns normal vector of this shape on a position'''
		pass
		
	def color_at(self,position):
		pass

class Plane(Object):
	
	def __init__(self,material,normal,intercept):
		super().__init__(material)
		self.math_repr = geo.Plane(normal,intercept)

	def intersection(self,ray):
		return self.math_repr.intersection(ray)

	def normal_at(self,position):
		return self.math_repr.normal
	
	def color_at(self,position):
		return self.material.color


class CheckerboardUpPlane(Plane):
	
	def __init__(self,material,intercept,cell_size,cell_color):
		super().__init__(material,geo.Vector(0,1,0),intercept)
		self.cell_size = cell_size
		self.cell_color = cell_color
	
	def color_at(self,position):
		checker=math.floor(position.x/self.cell_size)+math.floor(position.z/self.cell_size)
		if checker%2 == 0:
			return self.material.color
		else:
			return self.cell_color

class Sphere(Object):	
	
	def __init__(self,material,position,radius):
		super().__init__(material)
		self.math_repr = geo.Sphere(position,radius)

	def intersection(self,ray):
		return self.math_repr.intersection(ray)

	def normal_at(self,position):
		return (position-self.math_repr.position).normalize()
	
	def color_at(self,position):
		return self.material.color
