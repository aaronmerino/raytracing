from camera import Camera
from tkinter import Tk, Canvas, Frame, BOTH
from surface import Surface
from sphere  import Sphere
from triangle  import Triangle
from vector3 import Vec3
from ray import Ray
import math

WIDTH = 400
HEIGHT = 400
MAX_RENDER_DIST = 1000000

def hit(ray: Ray, objects: list, obj_ignore: Surface):
    obj_hit = None
    t = MAX_RENDER_DIST
    n = None

    for o in objects:
        res = o.hit(ray)
        if (res[0]):
            tr = res[1].ts[0]
            if (tr < t):
                t = tr
                obj_hit = o
                n = res[1].ns[0]
    return (obj_hit, t, n)

def rayColor(ray: Ray, objects: list, depth: int, obj_ignore: Surface):
    if depth == 5:
        return (0, 0, 0)

    obj_hit, t, n = hit(ray, objects, obj_ignore)

    if (obj_hit):
        lightsource = Vec3(-50, 20, 50)
        lightsource_dir = (lightsource - ray.getPoint(t)).normalize()
        shadow_ray = Ray(ray.getPoint(t), lightsource_dir)
        SHADOWED = False

        # hex_fill = None

        for o in objects:
            res = o.hit(shadow_ray)
            if (res[0]):
                SHADOWED = True
                break
        
        if (not SHADOWED):
            h = ((ray.dir.scale(-1)) + lightsource_dir).normalize()
            reflection_dir = ray.dir - n.scale(2*ray.dir.dot(n))
            reflection = Ray(ray.getPoint(t), reflection_dir)
            rec_ref = rayColor(reflection, objects, depth+1, obj_hit)
            Lr = min(int((0.1 * 4.5 * max(0,  n.dot(lightsource_dir)) + 0.5 * 4.5 * max(0, n.dot(h)**8) + 2*rec_ref[0]/255) * 255), 255)
            Lg = min(int((0.3 * 3 * max(0,  n.dot(lightsource_dir)) + 0.5 * 3 * max(0, n.dot(h)**8) + 2*rec_ref[1]/255) * 255), 255)
            Lb = min(int((0.6 * 0.3 * max(0,  n.dot(lightsource_dir)) + 0.5 * 0.3 * max(0, n.dot(h)**8) + 2*rec_ref[2]/255) * 255), 255)

            return (Lr, Lg, Lb)

        else:
            h = ((ray.dir.scale(-1)) + lightsource_dir).normalize()
            # print(ray.getPoint(t))
            Lr = min(int(0.1 * 4.5 * max(0,  n.dot(lightsource_dir)) * 255), 255)
            Lg = min(int(0.3 * 3 * max(0,  n.dot(lightsource_dir)) * 255) , 255)
            Lb = min(int(0.3 * 0.3 * max(0,  n.dot(lightsource_dir)) * 255) , 255)

            return (Lr, Lg, Lb)

   
    return (0 , 0, 0)
        
class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("ray tracing test")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.create_rectangle((5, 5)*2,
            outline="", fill="#8c8c8c")
        
        #  def __init__(self, origin: Vec3, focal_length: float, view_dir: Vec3, l: int, r: int, b: int, t: int):
        cam_pos = Vec3(0,10,-20)
        cam_dir = Vec3(0,1,0.1)
        cam = Camera(cam_pos, 100, cam_dir, -WIDTH//2, WIDTH//2, -HEIGHT//2, HEIGHT//2)
        objects = []

        # sphere = Sphere(Vec3(0, 100, 0), 50)
        objects.append(Sphere(Vec3(0, 100, 0), 50))
        objects.append(Sphere(Vec3(-12, 60, -20), 10))
        objects.append(Sphere(Vec3(-12, 60, 20), 10))
        objects.append(Sphere(Vec3(12, 60, 20), 10))
        objects.append(Sphere(Vec3(-12, 80, 40), 10))
        objects.append(Triangle(Vec3(0, 60, -30), Vec3(40, 60, -20), Vec3(10, 60, 10)))
        objects.append(Triangle(Vec3(0, 60, -30), Vec3(10, 40, -50), Vec3(40, 60, -20)))

        objects.append(Sphere(Vec3(-35, 34, 34), 5))

        objects.append(Triangle(Vec3(-50, 20, -80), Vec3(50, 20, -80), Vec3(-50, 200, -80)))
        objects.append(Triangle(Vec3(50, 20, -80), Vec3(50, 200, -80), Vec3(-50, 200, -80)))

        objects.append(Triangle(Vec3(-50, 20, 100), Vec3(-50, 200, 100), Vec3(50, 20, 100)))
        objects.append(Triangle(Vec3(50, 20, 100), Vec3(-50, 200, 100), Vec3(50, 200, 100)))

        for i in range(0, WIDTH):
            for j in range(0, HEIGHT):
                ray = cam.compute_ray(i, j, WIDTH, HEIGHT)

                Lr, Lg, Lb = rayColor(ray, objects, 0, None)

                Lr = hex(Lr)[2:]
                Lg = hex(Lg)[2:]
                Lb = hex(Lb)[2:]
                
                if len(Lr) == 1:
                    Lr = '0'+ Lr
                if len(Lg) == 1:
                    Lg = '0'+ Lg
                if len(Lb) == 1:
                    Lb = '0'+ Lb
                
                hex_fill = '#' + Lr + Lg + Lb
                canvas.create_rectangle((i, j)*2, outline="", fill=hex_fill)

        canvas.pack(fill=BOTH, expand=1)


def main():

    root = Tk()
    ex = Example()
    root.geometry(str(WIDTH) + 'x' + str(HEIGHT))
    root.mainloop()


if __name__ == '__main__':
    #set PATH=C:\Users\AaronJin\AppData\Local\Programs\Python\Python38-32;%PATH%
    main()