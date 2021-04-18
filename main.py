import csv
import plotly.figure_factory as ff
import pandas as pd
import statistics
import plotly.graph_objects as go
import random

df=pd.read_csv("data.csv")
data=df["temp"].tolist()

# mean=statistics.mean(data)
# std_deviation=statistics.stdev(data)

# print("population_mean is",mean)
# print("std_deviation is",std_deviation)

# fig=ff.create_distplot([data],["temp"],show_hist=False)
# fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="MEAN"))
# fig.show()

# dataSet=[]

# for i in range (0,100):
#     random_index=random.randint(0,len(data))
#     value=data[random_index]
#     dataSet.append(value)

# mean=statistics.mean(dataSet)
# std_deviation=statistics.stdev(dataSet)

# print("population_mean is",mean)
# print("std_deviation is",std_deviation)

def random_set_of_mean(counter):
    dataSet=[]
    for i in range (0,counter):
        random_index=random.randint(0,len(data))
        value=data[random_index]
        dataSet.append(value)

    mean=statistics.mean(dataSet)
    return mean 

def show_fig(mean_list):
    df=mean_list
    mean=statistics.mean(mean_list)
    print("mean of sampling distribution is -->",mean)
    fig=ff.create_distplot([df],["temp"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="MEAN"))
    fig.show()

def setup():
    mean_list=[]
    for i in range(0,1000):
        set_of_mean=random_set_of_mean(100)
        mean_list.append(set_of_mean)
    show_fig(mean_list)

setup()

def standard_deviation():
    mean_list=[]
    for i in range(0,1000):
        set_of_mean=random_set_of_mean(100)
        mean_list.append(set_of_mean)
    std_deviation=statistics.stdev(mean_list)
    print("standard deviation of sampling distrubition is",std_deviation)

standard_deviation()
