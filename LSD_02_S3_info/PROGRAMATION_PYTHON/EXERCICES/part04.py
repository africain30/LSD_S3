#BOOTCAMP PYTHON
# LSD 2 : S3
# MODULE : INFO
# CHARAF YOUSRI 
# 04/DEC/2022


#EXERCICE 01
class square:
	def __init__(self , l):   
	  self.l=l
	def area(self):
		return (self.l)**2
	def perimeter(self):
		return (self.l)*4

a = square(10)
print( "the area of the square is : "  , a.area() )
print( "the perimeter of the square is : "  , a.perimeter() )
