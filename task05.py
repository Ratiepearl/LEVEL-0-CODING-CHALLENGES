from math import sqrt
def lengths_of_triangle(side1,side2,side3):
    s = (side1+side2+side3)/2
    area_triangle = sqrt((s*(s-side1)*(s-side2)*(s-side3)))
    return(area_triangle) 
#print(lengths_of_triangle(9,8,7))