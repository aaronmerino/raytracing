from __future__ import annotations
from surface import Surface
from surface import HitRec
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
            return (False, None)
        elif disc > 0:
            # two solutions
            t1 = ((d.scale(-1)).dot(e - c) - math.sqrt(disc))/d.dot(d)
            t2 = ((d.scale(-1)).dot(e - c) + math.sqrt(disc))/d.dot(d)
            n1 = self.normal(ray.getPoint(t1))
            n2 = self.normal(ray.getPoint(t2))

            # print(str(t1) + ', ' + str(t2))

            if t2 < 10**(-8):
                return (False, None)
            elif t1 < 10**(-8) and t2 >= 10**(-8):
                return (True, HitRec([t2], [n2]))
            elif t1 >= 10**(-8):
                return (True, HitRec([t1, t2], [n1, n2]))
        else:
            # one solution
            t1 = ((d.scale(-1)).dot(e - c))/d.dot(d)
            n1 = self.normal(ray.getPoint(t1))
            return (True, HitRec([t1], [n1]))
    
    def normal(self, p: Vec3):
        # if (p - self.origin).dot(p - self.origin) - self.radius**2 == 0:
        return ((p - self.origin).scale(2)).normalize()

    def boundingBox(self):
        return None