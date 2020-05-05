from __future__ import annotations
from vector3 import Vec3
from ray import Ray

class Surface:
    def __init__(self, origin: Vec3):
        self.origin = origin

    def hit(self, ray: Ray):
        return (False, None)
    
    def normal(self, p: Vec3):
        return None

    def boundingBox(self):
        return None

class HitRec:
    def __init__(self, ts: list, ns: list):
        self.ts = ts
        self.ns = ns