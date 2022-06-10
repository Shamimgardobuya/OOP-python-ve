#create class coz radius different,i
#def init function for unique attributes.
#create function for area and pass in self as parameters
#create variable for holding the area
#create function for holding circumference of circle 
#pass in self
#create variable for holding circumference
#return and end function
    #create class square
    #def init for the unique attribute of the side of the square
    #create function  for area and pass in self as parameter
    #area is side square
    #create function for perimtere,pass in self as parameter
    #create variable to hold the perimter
    #return area and parameter
    #End function
#create class rectangle and use a def init
#use def init and pass in self with length and width
#create fnuction area and pass in self as paramter
#create variable holding length by width
#create function holding parameter and pass in self as parameter
#create variable holding perimeter 2(l+w)
#return
#End function
   #create class sphere and inside it have  a def init and pass in self and r
   #create function of area and pass in self as parameter
   #create variable hollding area is 4prsq
   #create function volume and pass in self as paramtert
   #create variable to holding volume
   #return volume
   #End function
   
    
    
from cmath import sqrt
from inspect import Parameter


class Circle:
    def __init__(self,r):
        self.r=r
    def arear(self):
        pi=3.14
        area=pi*self.r*self.r
        return f"  this is the area of the circle {area}cm "
    def circumference(self):
        z=3.147
        circum=2*z*self.r
        return f"this is the circumference of the circle {circum}cm"
class Square:
    def __init__(self,length):
        self.length=length
    def area_sq(self):
        square=self.length*self.length
        return f"{square}cmsq is the area of square"
    def peri(self):
        parameter=self.length*4
        return f"{parameter}cm is the parameter of the square"
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area_rec(self):
        rectangle=self.length*self.width
        return f"{rectangle}cmsq is the area of your rectangle"
    def perim_eter(self):
        total=self.length+self.width
        total_rect=2*total
        return f"{total_rect}cm is the perimeter of rectangle"
class Sphere:
    def __init__(self,radius):
        self.radius=radius
    def sphere_area(self):
        pi=3.142
        area=4*pi*self.radius*self.radius
        return f"{area}msq is the area of  sphere"
    def sphere_vol(self):
        pi=3.142
        volume=4/3*pi*self.radius*self.radius*self.radius   #we can use  3asterix 
        return f"{volume}m3  is the volume of sphere"
class Cone:
    def __init__(self,radius,height):
        self.radius=radius
        self.height=height
    def area(self):
        z=3.142*self.radius
        arear=self.height*self.height*self.radius*self.radius
        root=self.radius +sqrt(arear)
        final=z*root
        return f"{final} is the area of your cone"
        
    
    
        
    
       
