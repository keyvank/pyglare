from ..math.geometry import Ray,Vector
from .objects import Plane,Sphere
from ..image.color import Color
from .light import PointLight,AmbientLight,DirectionalLight,CircularSpotLight
from multiprocessing import Process,Manager
from threading import Thread
import math

class Engine:
	
	BIAS = 0.0000001
	
	def __init__(self,eye,environment,frame,max_depth,num_thread):
		self.eye = eye
		self.environment = environment
		self.frame = frame
		self.max_depth = max_depth
		self.num_thread = num_thread
		self._ambient_lights = [l for l in self.environment.lights if type(l) is AmbientLight]
		self._point_lights = [l for l in self.environment.lights if type(l) is PointLight]
		self._directional_lights = [l for l in self.environment.lights if type(l) is DirectionalLight]
		self._circular_spot_lights = [l for l in self.environment.lights if type(l) is CircularSpotLight]
	
	def _render_range(self,start,end,rows):
		for h in range(start,end):
			row=[]
			for w in range(self.frame.width):
				row.append(self._trace_ray(self.eye.corresponding_ray((self.frame.width,self.frame.height),(w,h)),0))
			rows.append(row)
	
	def render(self):
		step=self.frame.height / self.num_thread
		ranges=[]
		for i in range(self.num_thread-1):
			ranges.append((int(i*step),int(i*step+step)))
		ranges.append((int((self.num_thread-1)*step),int(self.frame.height)))
		m=Manager()
		rows={i:m.list() for i in range(self.num_thread)}
		threads=[]
		for i in range(len(ranges)):
			threads.append(Process(target=self._render_range,args=(ranges[i][0],ranges[i][1],rows[i])))
		for t in threads:
			t.start()
		for t in threads:
			t.join()
		
		del self.frame.data[:]
		
		for i in range(len(rows)):
			self.frame.data.extend(rows[i])

	def _is_in_shadow(self,ray,target):
		for obj in self.environment.objects:
			landa=obj.intersection(ray)
			if landa:
				if target:
					dist=(target-ray.position).length()
					if dist<landa:
						return False
					else:
						return True
				return True
		return False

	def _trace_ray(self,ray,depth,from_inside=False):
		
		if depth > self.max_depth:
			return Color(0,0,0)
		
		least_landa=None
		nearest_obj=None
		for obj in self.environment.objects:
			landa=obj.intersection(ray)
			if landa:
				if not least_landa or landa<least_landa:
					least_landa=landa
					nearest_obj=obj
		
		ret = Color(0,0,0)
		if not nearest_obj:
			return ret
		
		
		
		if least_landa:
			
			pos=ray.position + ray.direction*least_landa
			col=nearest_obj.color_at(pos)
			
			for l in self._ambient_lights:
				ret=ret+l.color*col
			
			norm=nearest_obj.normal_at(pos)
			if from_inside:
				norm = -norm
			pos = pos + norm * Engine.BIAS # Solving surface acne problem!
			
			for l in self._point_lights:
				light_ray_dir=(l.position-pos).normalize()
				if not self._is_in_shadow(Ray(pos,light_ray_dir),l.position):
					
					specular_factor=max(Vector.dot(norm.reflect(light_ray_dir),-ray.direction),0) ** nearest_obj.material.specular_exponent * nearest_obj.material.specular_rate
					
					diffuse_factor=max(Vector.dot(light_ray_dir,norm),0) * nearest_obj.material.diffuse_rate
					
					factor=diffuse_factor + specular_factor
					dist=(l.position-pos).length()
					atten=1.0/(l.atten_factors[0]+l.atten_factors[1]*dist+l.atten_factors[2]*dist*dist)
					
					ret = ret+l.color*l.intensity*col*factor*atten
			
			for l in self._directional_lights:
				light_ray_dir=-l.direction
				if not self._is_in_shadow(Ray(pos,light_ray_dir),None):
					
					specular_factor=max(Vector.dot(norm.reflect(light_ray_dir),-ray.direction),0) ** nearest_obj.material.specular_exponent * nearest_obj.material.specular_rate
					
					diffuse_factor=max(Vector.dot(light_ray_dir,norm),0) * nearest_obj.material.diffuse_rate
					
					factor=diffuse_factor + specular_factor
					
					ret = ret+l.color*l.intensity*col*factor
			
			for l in self._circular_spot_lights:
				light_ray_dir=(l.position-pos).normalize()
				if not self._is_in_shadow(Ray(pos,light_ray_dir),l.position):
					
					ang = math.acos(Vector.dot(light_ray_dir,-l.direction))
					if ang < l.angle/2:
					
						specular_factor=max(Vector.dot(norm.reflect(light_ray_dir),-ray.direction),0) ** nearest_obj.material.specular_exponent * nearest_obj.material.specular_rate
						
						diffuse_factor=max(Vector.dot(light_ray_dir,norm),0) * nearest_obj.material.diffuse_rate
						
						factor=diffuse_factor + specular_factor
						dist=(l.position-pos).length()
						atten=1.0/(l.atten_factors[0]+l.atten_factors[1]*dist+l.atten_factors[2]*dist*dist)
						
						ret = ret+l.color*l.intensity*col*factor*atten
			
			if nearest_obj.material.reflection_rate:
				addcol=col*self._trace_ray(Ray(pos,norm.reflect(-ray.direction)),depth+1) * nearest_obj.material.reflection_rate
				ret = ret + addcol
			
		return ret
