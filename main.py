from camera import Camera
from tkinter import Tk, Canvas, Frame, BOTH
from surface import Surface
from sphere  import Sphere
from vector3 import Vec3

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
        sphere = Sphere(Vec3(20, 100, 50), 50)

        for i in range(0, 800):
            for j in range(0, 800):
                ray = cam.compute_ray(i, j, 800, 800)

                res = sphere.hit(ray)
                if (res[0]):
                    canvas.create_rectangle((i, j)*2, outline="", fill="#%02x%02x%02x" % (109, 170, 44))
                


        canvas.pack(fill=BOTH, expand=1)


def main():

    root = Tk()
    ex = Example()
    root.geometry("800x800")
    root.mainloop()


if __name__ == '__main__':
    #set PATH=C:\Users\AaronJin\AppData\Local\Programs\Python\Python38-32;%PATH%
    main()