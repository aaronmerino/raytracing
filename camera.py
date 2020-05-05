from __future__ import annotations
from vector3 import Vec3
from ray import Ray

class Camera:
    def __init__(self, origin: Vec3, focal_length: float, view_dir: Vec3, l: int, r: int, b: int, t: int):
        self.origin = origin
        self.focal_length = focal_length
        self.view_dir = view_dir.normalize()
        self.l = l
        self.r = r
        self.b = b
        self.t = t
        # Construct coordienate frame for camera (2.4.7)
        self.w = self.view_dir.scale(-1)

        up_vector = Vec3(0,0,1)
        self.u = up_vector.cross(self.w)
        self.u = self.u.normalize()

        self.v = self.w.cross(self.u)

    def compute_ray(self, i: int, j: int, nx: int, ny: int) -> Vec3:
        u_scale = self.l + (self.r - self.l)*i/nx + (self.r - self.l)*0.5/nx
        v_scale = self.t - (self.t - self.b)*j/ny + (self.t - self.b)*0.5/ny

        return Ray(self.origin, self.view_dir.scale(self.focal_length) + self.u.scale(u_scale) + self.v.scale(v_scale))
        