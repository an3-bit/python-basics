#functions
from datetime import date


def calc_area_triangle(b,h):
    area = 0.5 *b*h
    print(area)
def calc_area_circle(radius):
    area = 22/7 *radius*radius
    area = round(area,2)
    print("Area of a circle is", area, "cm^2")

def print_todays_date ():
    today =date.today()
    print(today)

def add(*args):
    total=0
    for num in args:
        total +=num
        print("Total is ", total)

def sayHi(name,age=21):
    print("Hello", name, " I am", age, " years old")


sayHi("Mary")
sayHi("Kevo", 23)
calc_area_triangle(8,13)
calc_area_triangle(40, 66)

triangles = [[12,16], [14, 25], [13, 44], [6,13],[21,54]]

for t in triangles:
    calc_area_triangle(t[0],t[1])

calc_area_circle(2.76)
add(1,2)
add(23,46)
