from .geometry import Vector
from math import sin,cos

class Matrix:
	
	def __init__(self,rows):
		if rows:
			self.rows = rows
		else:
			self.rows = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

	def transform(self,vector):
		x = self.rows[0][0] * vector.x + self.rows[0][1] * vector.y + self.rows[0][2] * vector.z
		y = self.rows[1][0] * vector.x + self.rows[1][1] * vector.y + self.rows[1][2] * vector.z
		z = self.rows[2][0] * vector.x + self.rows[2][1] * vector.y + self.rows[2][2] * vector.z
		return Vector(x,y,z)
	
	def scale(factor):
		if isinstance(factor,Vector):
			return Matrix([[factor.x,0,0,0],[0,factor.y,0,0],[0,0,factor.z,0],[0,0,0,1]]
		else:
			return Matrix([[factor,0,0],[0,factor,0],[0,0,factor]]
	
	def translate(vector):
		return Matrix([[1,0,0,vector.x],[0,1,0,vector.y],[0,0,1,vector.z],[0,0,0,1]])
	
	def rotate_x(angle)(
		return Matrix([[1, 0, 0, 0],[0, cos(angle), -sin(angle), 0],[ 0, sin(angle), cos(angle), 0],[ 0, 0, 0, 1]]);
	
	def rotate_y(angle)(
		return Matrix([[cos(angle), 0, sin(angle), 0],[ 0, 1, 0, 0],[ -sin(angle),0, cos(angle), 0],[ 0, 0, 0, 1]]);
	
	def rotate_z(angle)(
		return Matrix([[cos(angle), -sin(angle), 0, 0],[ sin(angle), cos(angle), 0, 0],[ 0, 0, 1, 0],[ 0, 0, 0, 1]]);
	
