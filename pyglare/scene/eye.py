from ..math.geometry import Vector,Ray
import math

class Eye:
	
	def __init__(self,position,direction,up,aspect_ratio,field_of_view = math.pi/4):
		self.position = position
		self.direction = direction
		self.up = up
		self.aspect_ratio = aspect_ratio
		self.field_of_view = field_of_view
		
		self._height = math.tan(self.field_of_view/2) * 2
		self._width = self.aspect_ratio * self._height
		
		self._rv = Vector.cross(self.up,self.direction).normalize()
		self._uv = Vector.cross(self.direction,self._rv).normalize()
		
		self._ld = self.position + self.direction + -self._rv*self._width/2 + -self._uv*self._height/2
		
	def corresponding_ray(self,frame_size,pixel_index):
		pixel_pos = self._ld + self._rv * (pixel_index[0]/frame_size[0]*self._width) + self._uv * (pixel_index[1]/frame_size[1]*self._height)
		
		return Ray(self.position,(pixel_pos-self.position).normalize())
	
	def create_lookat(position,target,up,aspect_ratio,field_of_view = math.pi/4):
		return Eye(position,(target-position).normalize(),up,aspect_ratio,field_of_view)
