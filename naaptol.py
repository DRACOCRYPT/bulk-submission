from tkinter import E
import plotly.figure_factory as ff 
import statistics
import random

dice_result=[]
for i in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice_result.append(dice1+dice2)

mean=sum(dice_result)/len(dice_result)
median=statistics.median(dice_result)
mode=statistics.mode(dice_result)
stdev=statistics.stdev(dice_result)

print("mean of the data is: " ,mean)
print("median of the data is: " ,median)
print("mode of the data is: " ,mode)
print("stdevof the data is: " ,stdev)
 
fig = ff.create_distplot([dice_result],["Result"],show_hist=False)
fig.show()