from math import tan, pi
n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))
p = n * (s ** 2) / (4 * tan(pi / n))
print("The area of the polygon is: ", int(p))