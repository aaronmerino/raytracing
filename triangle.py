from __future__ import annotations
from surface import Surface
from surface import HitRec
from vector3 import Vec3
from ray import Ray
import math

class Triangle(Surface):
    def __init__(self, a: Vec3, b: Vec3, c: Vec3):
        self.a = a
        self.b = b
        self.c = c

    def hit(self, ray: Ray):
        xa = self.a.x
        ya = self.a.y
        za = self.a.z

        xb = self.b.x
        yb = self.b.y
        zb = self.b.z

        xc = self.c.x
        yc = self.c.y
        zc = self.c.z

        xd = ray.dir.x
        yd = ray.dir.y
        zd = ray.dir.z

        xe = ray.origin.x
        ye = ray.origin.y
        ze = ray.origin.z

        a = xa - xb
        b = ya - yb
        c = za - zb
        d = xa - xc
        e = ya - yc
        f = za - zc

        g = xd
        h = yd 
        i =  zd
        j = xa - xe
        k = ya - ye 
        l = za - ze

        M = a*(e*i - h*f) + b*(g*f - d*i) + c*(d*h - e*g)
        
        t = -1* (f*(a*k - j*b) + e*(j*c - a*l) + d*(b*l - k*c))/M
        if (t < 0): 
            # print('here1')
            return (False, None)

        gamma = (i*(a*k - j*b) + h*(j*c - a*l) + g*(b*l - k*c))/M
        if (gamma < 0 or gamma > 1):
            # print('here2')
            return (False, None)

        beta = (j*(e*i - h*f) + k*(g*f - d*i) + l*(d*h - e*g))/M
        if (beta < 0 or beta > 1 - gamma):
            # print('here3')
            return (False, None)

        n = self.normal(ray.getPoint(t))

        return (True, HitRec([t], [n]))
        

    def normal(self, p: Vec3):
        return ((self.b - self.a).cross(self.c - self.a)).normalize()

    def boundingBox(self):
        return None
    

        