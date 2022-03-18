import pandas as pd
import csv 
import statistics
import random
import plotly.figure_factory as ff 
import plotly.graph_objects as go 

df = pd.read_csv("py5.csv")
data=df["average"].tolist()


def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df=mean_list
    mean=statistics.mean(df)
    fig=ff.create_distplot([df],['average'],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="MEAN"))
    fig.show()

def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_means=random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)

    mean=statistics.mean(mean_list)
    print("Mean of sampling ditribution ",mean)

setup()

population_mean = statistics.mean(data)
print("population mean that means the whole mean",population_mean)

def standard_deviation():
    mean_list=[]
    for i in range(0,1000):
        set_of_means=random_set_of_mean(100)
        mean_list.append(set_of_means)
    standard_deviation=statistics.stdev(mean_list)
    print("Standaed deviation of sampling ditribution ",standard_deviation)

standard_deviation()