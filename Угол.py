import math

def find_angles(a, b, c):
    angle_A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
    
    angle_B = math.degrees(math.acos((c**2 + a**2 - b**2) / (2 * c * a)))
    
    angle_C = 180 - angle_A - angle_B
    
    return angle_A, angle_B, angle_C

a = 5
b = 7
c = 8

angle_A, angle_B, angle_C = find_angles(a, b, c)

print("Угол A:", angle_A)
print("Угол B:", angle_B)
print("Угол C:", angle_C)