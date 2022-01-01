#CHARAF YOUSRI
#LSD_2 : S3
#MODULE : INFORMATIQUE
#LE 02/DEC/2021


#serie 01



#exercice 01
def get_slice(a,n,m):
  print("la longueur de cette string est  : " ,len(a))
  if(n>=m):
    print('ERROR')
    return;
  print(a[n:m])

a="ce string est just pour les test"
get_slice(a,3,15);
print("-----------------------------------------")




#exercice 03
def dictionary2(test):
  dictio = {}
  for i in test:
    if i in dictio:
        dictio[i] += 1
    else:
        dictio[i] = 1  
  print(str(dictio))   

dictionary2(a)
print("-----------------------------------------")




#exercice 04
def two_lists(a,b):
  if(len(a)!=len(b)):
    print("ERROR")
    return
  for i in range(len(a)):
    print(a[i]," ",b[-1- i],'\n')

two_lists(numbers_x,numbers_y)
print("-----------------------------------------")




#exercice 05
import numpy as np
a = np.ones((1, 10)).reshape(2, -1)
b = np.zeros((1, 10)).reshape(2, -1)
c = np.concatenate((a,b),axis=1)
print(a);
print(b);
print(c);
print("-----------------------------------------")




#exercice 06
a = np.arange(3)
b = np.ones((3,3,3))
print(a);
print(b);
test3= np.ones((3,9))
print(test3)

