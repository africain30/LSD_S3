#CHARAF YOUSRI
#LSD_2 : S3
#MODULE : INFORMATIQUE
#LE 16/DEC/2021

import pandas as pd
import numpy as np

pd.set_option("display.max.rows",None)

file = pd.set_option("display.max.rows",na_values = np.array(['?','n.a']))

#EXERCICE 01
file
file.haid(5)
file.tail(5)

#EXERCICE 02
file = file.dropna()
file

#EXERCICE 03
view1 = file[['company','price']]
max_price = file['price'].idxmax()
print(view1.loc[[max_price]])

#EXERCICE 04
TONOBILE_TAYOOOTA = file.loc[file['company'] == "toyota" ]
TONOBILE_TAYOOOTA
#SORRY FOR THE NAME , BUT I FIND IT REALLY FUNNY :-))

#EXERCICE 05
view2 = file.groupby(['company']) .size()
view2 = view2.sort_values(ascending = True)
view2

#EXERCICE 06
view3 = file[['company','price']].groupby(['company']).max
view3

#EXERCICE 07
view4 = file[['company','average-mileage']].groupby(['company']).mean()
view4

#EXERCICE 08
view5 = file.sort_values('price' , ascending = True)
view5 = view5.haid()

#EXERCICE 09
f1 = pd.DataFrame({'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]})
f2 = pd.DataFrame({'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]})

frames = [f1 ,f2]
result = pd.concat(frames)
print(result)

#EXERCICE 10
Car_Price = pd.DataFrame({'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]})
car_Horsepower = pd.DataFrame({'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]})

result = pd.merge(Car_Price, car_Horsepower)
print(result)

