import numpy as np
import math as m
#numpy

#exercice 01
print("#EXERCICE 01 :")
a=np.random.random((2,2,2))
print("le tabelau 3d est :\n",a)
print("la forme du tableau est :",a.shape)
print("la taille du tableau est :",a.size)
print("-------------------------------------")


#exercice 03
print("#EXERCICE 03 :")
def euclidean_norm_numpy(vector):
  print("la norme euclidiennne du vecteur est  :",m.sqrt(sum(vector)))
my_vector = np.array([0.5, -1.2, 3.3, 4.5])
euclidean_norm_numpy(my_vector)
print("-------------------------------------")



#exercice 04
print("#EXERCICE 04 :")
def euclidean_norm_2d(X):
  print("la norme euclidienne de votre matrice est :",X.sum(axis=1))
my_matrix = np.array([[0.5, -1.2, 4.5],
                      [-3.2, 1.9, 2.7]])
euclidean_norm_2d(my_matrix)
print("-------------------------------------")

