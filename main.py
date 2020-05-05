from camera import Camera
from tkinter import Tk, Canvas, Frame, BOTH
from surface import Surface
from sphere  import Sphere
from vector3 import Vec3
import math

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("ray tracing test")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.create_rectangle((5, 5)*2,
            outline="", fill="#fb0")
        
        #  def __init__(self, origin: Vec3, focal_length: float, view_dir: Vec3, l: int, r: int, b: int, t: int):
        cam = Camera(Vec3(0,0,0), 100, Vec3(0,1,0), -400, 400, -400, 400)
        objects = []

        # sphere = Sphere(Vec3(0, 100, 0), 50)
        objects.append(Sphere(Vec3(0, 100, 0), 50))
        objects.append(Sphere(Vec3(-12, 60, -20), 10))
        objects.append(Sphere(Vec3(-12, 60, 20), 10))
        objects.append(Sphere(Vec3(12, 60, 20), 10))
        objects.append(Sphere(Vec3(-12, 80, 40), 10))

        for i in range(0, 800):
            for j in range(0, 800):
                ray = cam.compute_ray(i, j, 800, 800)
                
                obj_hit = None
                t = 1000000
                n = None
                for o in objects:
                    res = o.hit(ray)
                    if (res[0]):
                        tr = res[1].ts[0]
                        if (tr < t):
                            t = tr
                            obj_hit = o
                            n = res[1].ns[0]

                # res = o.hit(ray)
                # if (res[0]):
                if (obj_hit):
                    # n = res[1].ns[0]
                    # t = res[1].ts[0]

                    lightsource = Vec3(-50, 20, 50)
                    lightsource_dir = (lightsource - ray.getPoint(t)).normalize()
                    # print(ray.getPoint(t))
                    Lr = min(int((0.4 * 3 * max(0,  n.dot(lightsource_dir))) * 255), 255)
                    Lg = min(int((0.3 * 2 * max(0,  n.dot(lightsource_dir))) * 255), 255)
                    Lb = min(int((0.4 * 0.2 * max(0,  n.dot(lightsource_dir))) * 255), 255)

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

                    #"#" + hex(Lr)[2:] + hex(Lg)[2:] + hex(Lb)[2:]
                    
                    
                    canvas.create_rectangle((i, j)*2, outline="", fill=hex_fill)
                


        canvas.pack(fill=BOTH, expand=1)


def main():

    root = Tk()
    ex = Example()
    root.geometry("800x800")
    root.mainloop()


if __name__ == '__main__':
    #set PATH=C:\Users\AaronJin\AppData\Local\Programs\Python\Python38-32;%PATH%
    main()