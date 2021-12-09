import matplotlib.pyplot as plt
import numpy as np
import math as m

#exercice 01
print("#EXERCICE 01 :\n")
def pie_chart():
  my_values = np.array([29.1,16.5,24.3,20.4,9.7])
  my_label=["C","C++","JAVA","PYTHON","PHP"]
  my_explode=[0.1,0,0,0,0]

  plt.title("     Popularity of Programming Language\n")
  plt.pie(my_values , labels = my_label , explode = my_explode , autopct='%1.1f%%' , shadow =True)
  plt.show()
pie_chart()
print("-------------------------------------")
#exercice 02
def line_chart():
  x=["03 oct 2016","04","05","06","7"]
  y_open=[774.25,776.030029,779.309998,779,779.659973]
  y_high=[776.065002,778.710022,782.070007,780.47998,779.659973]
  y_low=[769.5,772.890015,775.650024,775.539978,770.75]
  y_close=[772.559998,776.429993,776.469971,776.859985,775.080017]
  plt.plot(x,y_open,label="open")
  plt.plot(x,y_high,label="high")
  plt.plot(x,y_close,label="close")
  plt.plot(x,y_low,label="low")
  plt.xlabel("date")
  plt.legend()
  plt.show()
line_chart()
