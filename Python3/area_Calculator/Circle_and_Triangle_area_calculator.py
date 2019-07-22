"""A program that calculates the area of 
a triangle or circle"""

print("Calculator is starting")

option = input("Enter C for Circle or T for Triangle: ")

if option == "C":
  radius = float(input("Enter the radius of the circle: "))
  area = 3.13159 ** 2
  print("The area is %s" % (area))
elif option == "T":
  base =float(input("Enter the base of the triangle: "))
  height = float(input("Enter the height of the triangle: "))
  area = 0.5 * base * height
  print("The area of the triangle is %s" % (area))
else:
  print("Not a Valid input")
  
  
print("The calculator has done his job, now Exiting")
