from __future__ import annotations
from vector3 import Vec3

class Ray:
    def __init__(self, origin: Vec3, dir: Vec3):
        self.origin = origin
        self.dir = dir.normalize()

    def getPoint(self, t):
        return self.origin + self.dir.scale(t)