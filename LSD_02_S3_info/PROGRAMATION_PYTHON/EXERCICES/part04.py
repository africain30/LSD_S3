#BOOTCAMP PYTHON
# LSD 2 : S3
# MODULE : INFO
# CHARAF YOUSRI 
# 04/DEC/2022


#EXERCICE 01
class square:
	def __init__(self , l , L):  
		if type(l)!=int() and type(l)!= float():
      			raise ValueError 
		self.l = l
		self.L = L
	def area(self):
		return (self.l)**2
	def perimeter(self):
		return (self.l)*4
	
#EXERCICE 02
class rectangle(square):
	def __init__(self , l , L):
		super().__init__(l = l , L = L)
		self.l = l
		self.L = L
	def area_rec(self):
    return (self.L) * (self.l)
  def perimeter_rec(self):
    return (self.l + self.L) * 2 



a = square( 10 , 10 )
b = rectangle( 10 , 10 )
print( "the area of the square is : "  , a.area() )
print( "the perimeter of the square is : "  , a.perimeter() )
print( "the area of the rectangle  is : "  , a.area_rec() )
print( "the perimeter of the rectagle is : "  , a.perimeter_rec() )
