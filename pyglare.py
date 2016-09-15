#!/usr/bin/python3

from pyglare.image.ppm import save
from pyglare.image.frame import Frame
from pyglare.image import color
from pyglare.scene.eye import Eye
from pyglare.scene.engine import Engine
from pyglare.scene.environment import Environment
from pyglare.scene.objects import Material
from pyglare.scene.objects import Plane,CheckerboardUpPlane,Sphere
from pyglare.math import geometry as geo
from pyglare.scene.light import PointLight,AmbientLight,DirectionalLight,CircularSpotLight
import math

if __name__ == '__main__':
	f = Frame(2000,2000,color.BLACK)
	env = Environment()
	
	env.objects.append(CheckerboardUpPlane(Material(color.WHITE,1,0.1,1,0.3),200,200,color.BLACK))
	env.objects.append(Sphere(Material(color.RED,1,1,8,0.5),geo.Vector(140,-100,0),100))
	env.objects.append(Sphere(Material(color.YELLOW,1,1,8,0.5),geo.Vector(0,0,450),200))
	env.objects.append(Sphere(Material(color.GREEN,1,1,8,0.5),geo.Vector(-140,-90,0),110))
	
	env.lights.append(AmbientLight(color.Color(0.05,0.05,0.05)))
	env.lights.append(DirectionalLight(color.Color(0.1,0.1,0.1),geo.Vector(1,-1,1).normalize(),6))
	
	e = Eye.create_lookat(geo.Vector(0,324,-532),geo.Vector(0,0,80),geo.Vector(0,1,0),f.width/f.height)
	
	eng = Engine(e,env,f,4,8)
	
	print('Rendering...')
	eng.render()
	print('Done! Saving...')
	
	save('result.ppm',f)
