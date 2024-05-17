'''032
Ask for the radius and the depth of a cylinder 
and work out the total volume (circle 
area*depth) rounded to three decimal 
places.'''
import math
radius=float(input('Input the radius of the cylinder'))
depth=float(input('Please input the depth of the cylinder'))
pi=math.pi
c_area=pi*radius*radius
volume=c_area*depth
print(round(volume,3))