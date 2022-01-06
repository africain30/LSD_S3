# LSD 2 : S3
# CHARAF YOUSRI 
# LE 04/01/2022

#EXERCICE 01
#Explain the reference of variables :

# Person : the class 
# person : variable of type Person (it is an object)
# surname : is a carracterestique of the variable person
# age :  is the age of the object "person"
# AGE : is a methode of the class "Person" that returns the age of "person"
# self.email =  
# person.email = 


#EXERCICE 02

#EXERCICE 03
#EXERCICE 04
class number():
  MULTIPLIER  = 5
  def __init__(self,x,y):
    if type(x) != int() or type(y) != int():
      self.x = x
      self.y = y
    else:
      raise ValueError;
  
  def add(self):
    return self.x + self.y

  def multiply(self, a):
        return self.MULTIPLIER * a
  
  def subtract(b,c):
        return b-c

  def value(self):
        return self.x, self.y


num = number(5,6)
print(num.add())
print(num.multiply(2))
print(num.subtract(2,4))
print(num.value())

#EXERCICE 05
