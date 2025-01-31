class Cylinder:
    def __init__(self,radius,height,color):
        self.r = radius
        self.h = height
        self.rangi = color
    def calc_area(self, is_closed = True):
        if is_closed:
            area = 2* 22/7 *self.r**2 + 2 * 22/7*self.r * self.h
            print(f"Area of close cylinder is : {area}")
        else:
            area = 2 * 22 / 7 * self.r ** 2 + 2 * 22 / 7 * self.r * self.h
            print(f"Area of open cylinder is : {area}")
    def calc_volume(self):
        v = 22/7 *self.r**2*self.h
        print(f"Vlume of the cylinder is : {v}")

c1 = Cylinder(10,11,"red")
c2 = Cylinder ( 7.8, 22.7, "blue")
c1.calc_area()
c1.calc_volume()
