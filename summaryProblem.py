import math

# calculate side length
def calculate_side(x1,y1,x2,y2):
    base = abs(x1 - x2)
    height = abs(y1 - y2)
    a2 = height * height
    b2 = base * base
    c2 = a2 + b2
    c = math.sqrt(c2)
    return c

#calculate side length as a square root
def calculate_side_as_square_root(x1,y1,x2,y2):
    base = abs(x1 - x2)
    height = abs(y1 - y2)
    a2 = height * height
    b2 = base * base
    c2 = a2 + b2
    return c2

# solve for X given two point-slope equations
def solveForX (m1,b1,m2,b2):
    eliminationSlope = m1 + -m2
    eliminationIntercept = b1 + -b2
    eliminationIntercept = -eliminationIntercept
    x = eliminationIntercept / eliminationSlope
    return x

def solveForY (m1,b1,x):
    y = (m1 * x) + b1
    return y

# function to convert fraction strings to floats
def convert_to_float(frac_str):
    try:
        return float(frac_str)
    except ValueError:
        num, denom = frac_str.split('/')
        try:
            leading, num = num.split(' ')
            whole = float(leading)
        except ValueError:
            whole = 0
        frac = float(num) / float(denom)
        return whole - frac if whole < 0 else whole + frac

# function to generate the opposite inverse of a given number
def opposite_inverse(number):
    return -(1/number)

# gather input
print("")
m1 = convert_to_float(input("Slope of L1: "))
b1 = convert_to_float(input("Y-intercept of L1: "))
print("")
m2 = convert_to_float(input("Slope of L2 (perpendicular to L1): "))
b2 = convert_to_float(input("Y-intercept of L2: "))
print("")
m3 = convert_to_float(input("Slope of L3 (perpendicular to L2, or same as L1): "))
b3 = convert_to_float(input("Y-intercept of L3 (can't be same as L1): "))
print("")
m4 = convert_to_float(input("Slope of L4 (perpendicular to L3, or same as L2): "))
b4 = convert_to_float(input("Y-intercept of L4 (can't be same as L2): "))
print("")

# validate inputs follow rules
got_one_wrong = False
if not m1 == m3:
    got_one_wrong = True
    print("L1 and L3 should be parallel.")
if not m2 == m4:
    got_one_wrong = True
    print("L2 and L4 should be parallel.")
if not m2 == opposite_inverse(m1):
    got_one_wrong = True
    print("L1 and L2 should be perpendicular.")
if not m3 == opposite_inverse(m2):
    got_one_wrong = True
    print("L2 and L3 should be perpendicular.")
if not m4 == opposite_inverse(m3):
    got_one_wrong = True
    print("L3 and L4 should be perpendicular.")
if not m1 == opposite_inverse(m4):
    got_one_wrong = True
    print("L1 and L4 should be perpendicular.")
if m1 == m3 and b1 == b3:
    got_one_wrong = True
    print("L1 and L3 should not be the same line.")
if m2 == m4 and b2 == b4:
    got_one_wrong = True
    print("L2 and L4 should not be the same line.")
if got_one_wrong:
    print("")
    print("Try again with better inputs.")
    quit()

# calculate intersections
print("=== INTERSECTIONS ===")
x1 = solveForX(m1,b1,m2,b2)
y1 = solveForY(m1,b1,x1)
print("Intersection L1-L2: ("+str(x1)+","+str(y1)+")")

x2 = solveForX(m2,b2,m3,b3)
y2 = solveForY(m2,b2,x2)
print("Intersection L2-L3: ("+str(x2)+","+str(y2)+")")

x3 = solveForX(m3,b3,m4,b4)
y3 = solveForY(m3,b3,x3)
print("Intersection L3-L4: ("+str(x3)+","+str(y3)+")")

x4 = solveForX(m4,b4,m1,b1)
y4 = solveForY(m4,b4,x4)
print("Intersection L4-L1: ("+str(x4)+","+str(y4)+")")
print("")

# calculate side lengths
print("=== SIDES ===")
s1 = calculate_side(x1,y1,x2,y2)
s1_as_square_root = calculate_side_as_square_root(x1,y1,x2,y2)
print("Length of L1-L2: "+str(s1)+" units (or, square root of "+str(s1_as_square_root)+")")

s2 = calculate_side(x2,y2,x3,y3)
s2_as_square_root = calculate_side_as_square_root(x2,y2,x3,y3)
print("Length of L2-L3: "+str(s2)+" units (or, square root of "+str(s2_as_square_root)+")")

s3 = calculate_side(x3,y3,x4,y4)
s3_as_square_root = calculate_side_as_square_root(x3,y3,x4,y4)
print("Length of L3-L4: "+str(s3)+" units (or, square root of "+str(s3_as_square_root)+")")

s4 = calculate_side(x4,y4,x1,y1)
s4_as_square_root = calculate_side_as_square_root(x4,y4,x1,y1)
print("Length of L4-L1: "+str(s4)+" units (or, square root of "+str(s4_as_square_root)+")")
print("")

#calculate area of object
area = s1 * s2

if s1 == s2 and s2 == s3 and s3 == s4:
    shape = "square"
else:
    shape = "rectangle"
print("=== AREA ===")
print("The area of this "+shape+" is "+str(area)+" units squared.")
print("")