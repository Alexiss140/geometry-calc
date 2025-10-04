# Geometry calc
import math


main = input("What do you want to calculate(area or volume)? ")
main = main.lower() 

if main == 'area':
    shape = input("Area of what shape?(square, rectangle, triangle, trapezoid, circle, cone, sphere, polygon) ")
    if shape == 'square':
        square = float(input("Enter side A "))
        Asquare = square * square
        print(f"Area of the square is {round(Asquare, 3)}")
    elif shape == 'rectangle':
        rsidea = float(input("Enter side A "))
        rsideb = float(input("Enter side B "))
        Arectangle = rsidea * rsideb
        print(f"Area of the recrangle is{round(Arectangle, 3)}")
    elif shape == 'triangle':
        tsidea = float(input("Enter side A "))
        tsideb = float(input("Enter side B "))
        Atriangle = tsidea * tsideb / 2
        print(f"Area of the triangle is {round(Atriangle, 3)}")
    elif shape == 'trapezoid':
        tsidelarge = float(input("Enter the large side "))
        tsidesmall = float(input("Enter the small side "))
        theight = float (input("Enter the height "))
        Atrapezoid = (tsidelarge + tsidesmall) / 2 * theight
        print(f"Area of the trapezoid is {round(Atrapezoid, 3)}")
    elif shape == 'circle':
        cradius = float(input("Enter the radius "))
        Acircle = math.pi * cradius ** 2
        print(f"Area of the circle is {round(Acircle, 3)}")
    elif shape == 'cone':
        coradius = float(input("Enter the radius "))
        coheight = float(input("Enter the height "))
        Acone = math.pi * coradius * coheight
        print(f"Area of the cone is {round(Acone, 3)}")
    elif shape == 'sphere':
        sradius = float(input("Enter the radius "))
        Asphere = 4 * math.pi * sradius ** 2
        print(f"Area of the sphere is {round(Asphere, 3)}")
    elif shape == 'polygon':
        pradius = float(input("Enter the radius "))
        papothem = float(input("Enter the apothem "))
        Apolygon = pradius / 2 * papothem
        print(f"Area of the polygon is {round(Apolygon, 3)}")
if main == 'volume':
    value = input("Value of what shape?(cube, parallelepiped, prism, cylinder) ")
    if value == 'cube':
        cside = float(input("Enter the side "))
        Vcube = cside ** 3
        print(f"Volume of the cube is {round(Vcube, 3)}")
    elif value == 'parallelepiped':
        psidea = float(input("Enter side A "))
        psideb = float(input("Enter side B "))
        psidec = float(input("Enter side C "))
        Vparallelepiped = psidea * psideb * psidec
        print(f"Volume of the parallelepiped is {round(Vparallelepiped, 3)}")
    elif value == 'regular prism':
        rpbase = float(input("Enter the base "))
        rpheight = float(input("Enter the height "))
        Vregularprism = rpbase * rpheight 
        print(f"Value of the regular prism is {round(Vregularprism, 3)}")
    elif value == 'cylinder':
        cradius = float(input("Enter the radius "))
        cheight = float(input("Enter the height"))
        Vcylinder = math.pi * cradius ** 2 * cheight
        print(f"Value of the cylinder is {round(Vcylinder, 3)}")