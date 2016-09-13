from ..math import geometry as geo
from ..image.color import Color
import math

class Material:
	
	def __init__(self,color,diffuse_rate,specular_rate,specular_exponent,reflection_rate,refraction_rate,refractive_index):
		self.color = color
		self.diffuse_rate = diffuse_rate
		self.specular_rate = specular_rate
		self.specular_exponent = specular_exponent
		self.reflection_rate = reflection_rate
		self.refraction_rate = refraction_rate
		self.refractive_index = refractive_index

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
		div=geo.Vector.dot(ray.direction,self.math_repr.normal)
		if div==0:	# Plane and ray are parallel!
			return None
		t = -(geo.Vector.dot(ray.position,self.math_repr.normal)+self.math_repr.intercept)/div
		if t>0:
			return t
		else:
			return None

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
		tca=geo.Vector.dot(self.math_repr.position-ray.position,ray.direction)
		if tca<0:
			return None
		d2=geo.Vector.dot(self.math_repr.position-ray.position,self.math_repr.position-ray.position)-tca*tca
		if d2 > self.math_repr.radius ** 2:
			return None
		thc=math.sqrt(self.math_repr.radius ** 2 - d2)
		ret=min(tca-thc,tca+thc)
		if ret<0:
			return None
		else:
			return ret

	def normal_at(self,position):
		return (position-self.math_repr.position).normalize()
	
	def color_at(self,position):
		return self.material.color
