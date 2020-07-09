In [46]:
X= float(input("Enter the length of any side: "))
Y= int(input("Enter the number of sides in the regular polygon: "))
import math
numerator= math.pow(X,2)*Y
denominator= 4*(math.tan(math.pi/Y))
area= numerator/denominator
print("The area of the regular polygon is:",area)