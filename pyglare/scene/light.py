class Light:
	
	def __init__(self,color):
		self.color = color

class AmbientLight(Light):
	
	def __init__(self,color):
		super().__init__(color)


class DirectionalLight(Light):
	def __init__(self,color,direction,intensity):
		super().__init__(color)
		self.direction = direction
		self.intensity = intensity


class PointLight(Light):
	def __init__(self,color,position,intensity,atten_factors = (1.,0.1,0.01) ):
		super().__init__(color)
		self.position = position
		self.intensity = intensity
		self.atten_factors = atten_factors

class CircularSpotLight(PointLight):
	def __init__(self,color,position,direction,intensity,angle):
		super().__init__(color,position,intensity)
		self.direction = direction
		self.angle = angle
