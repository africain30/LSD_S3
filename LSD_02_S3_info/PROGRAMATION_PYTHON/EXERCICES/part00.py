#exercice 02
def sum_mult(a,b):
  print("le produit de  ",a, "et " ,b, "est : ", a*b)
  print("la somme de  ",a, "et " ,b, "est : ", a+b)

sum_mult(5,3)
print("-----------------------------------------")



#exercice 03
print('Name', 'Is', 'James', sep='**')
print("-----------------------------------------")


#exercice 04
i=1
while(i<11):
  print(i,'\n')
  i=i+1
print("-----------------------------------------")


#exercice 05
a = ' '
for i in range(6):
	a = a +' {} '.format(i)
	print(a)
print("-----------------------------------------")



#exercice 06
def tablle_mult(a):
  for i in range(13):
    print(i," * ",a," = ",a*i,'\n')
tablle_mult(15)
print("-----------------------------------------")



#exercice 07
def test_product(a,b):
  if(a*b<1000):
    print( a," + ",b," = ",a+b)
  else:
    print( a," * ",b," = ",a*b)
test_product(50,50)
print("-----------------------------------------")



#exercice 08
def check_true(a):
  if(a[len(a)-1] == a[0]):
    print(True)
  else:
    print(False)

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

check_true(numbers_x);
check_true(numbers_y);
print("-----------------------------------------")
