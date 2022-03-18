import random
import statistics 
import pandas as pd
import plotly.figure_factory as ff 
import plotly.graph_objects as go 
import csv 

df=pd.read_csv("py6.csv")
data=df['Math_score'].tolist()
mean=statistics.mean(data)
stdev=statistics.stdev(data)
print("mean is ",mean)
print("standard deviation is ",stdev)



