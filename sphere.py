from __future__ import annotations
from surface import Surface
from vector3 import Vec3
from ray import Ray
import math

class Sphere(Surface):
    def __init__(self, origin: Vec3, radius: int):
        self.origin = origin
        self.radius = radius

    def hit(self, ray: Ray):
        c = self.origin
        e = ray.origin
        d = ray.dir
        r = self.radius

        # check discriminant
        disc =  (d.dot(e - c))**2 - (d.dot(d)) * ((e - c).dot(e - c) - r**2)

        if disc < 0:
            return (False, None, None)
        elif disc > 0:
            # two solutions
            t1 = ((d.scale(-1)).dot(e - c) - math.sqrt(disc))/d.dot(d)
            t2 = ((d.scale(-1)).dot(e - c) + math.sqrt(disc))/d.dot(d)

            return (True, t1, t2)
        else:
            # one solution
            t1 = ((d.scale(-1)).dot(e - c))/d.dot(d)
            return (True, t1, None)
    
    def boundingBox(self):
        return None