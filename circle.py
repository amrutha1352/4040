In [34]:
def area_of_circle(r):
   import math
   a=math.pi*r**2
   return a
 
 r=float(input('enter radius of a circle'))
 print("%.2f"%area_of_circle(r))