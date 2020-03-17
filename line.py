import math
x1 = int(input("What is X1? "))
y1 = int(input("What is Y1? "))
x2 = int(input("What is X2? "))
y2 = int(input("What is Y2? "))
slope = (x2 - x1) / (y2 - y1)
print("Slope is "+str(slope))
height = abs(x1 - x2)
base = abs(y1 - y2)
a2 = height * height
b2 = base * base
c2 = a2 + b2
c = math.sqrt(c2)
print("Line length is "+str(c)+" units.")