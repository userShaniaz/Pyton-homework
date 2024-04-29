# Прямоугольник
def rectangle_area(length, width):
    return length * width

def rectangle_perimeter(length, width):
    return 2 * (length + width)

length = 5
width = 3
print("Площадь прямоугольника:", rectangle_area(length, width))
print("Периметр прямоугольника:", rectangle_perimeter(length, width))

#Квадрат
def square_area(side):
    return side ** 2

def square_perimeter(side):
    return 4 * side

side_length = 5
print("Площадь квадрата:", square_area(side_length))
print("Периметр квадрата:", square_perimeter(side_length))


#Треугольник
def triangle_area(base, height):
    return 0.5 * base * height

def triangle_perimeter(a, b, c):
    return a + b + c

base = 4
height = 3
print("Площадь треугольника:", triangle_area(base, height))

a = 3
b = 4
c = 5
print("Периметр треугольника:", triangle_perimeter(a, b, c))

#Круг
import math

def circle_area(radius):
    return math.pi * radius**2

def circle_perimeter(radius):
    return 2 * math.pi * radius

radius = 5
print("Площадь круга:", circle_area(radius))
print("Периметр круга:", circle_perimeter(radius))

#Пареллелограмм
def parallelogram_area(base, height):
    return base * height

def parallelogram_perimeter(side, base):
    return 2 * (side + base)

base_length = 6
height_length = 4
print("Площадь параллелограмма:", parallelogram_area(base_length, height_length))

side_length = 5
print("Периметр параллелограмма:", parallelogram_perimeter(side_length, base_length))

#Трапеция
def trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

def trapezoid_perimeter(base1, base2, side1, side2):
    return base1 + base2 + side1 + side2

base1 = 6
base2 = 4
height = 3
print("Площадь трапеции:", trapezoid_area(base1, base2, height))

side1 = 5
side2 = 7
print("Периметр трапеции:", trapezoid_perimeter(base1, base2, side1, side2))
