import statistics
import random
import pandas as pd
import csv 
import plotly.figure_factory as ff
import plotly.graph_objects as go

df=pd.read_csv("newdata.csv")
data=df["average"].tolist()
population_mean=statistics.mean(data)
std_deviation=statistics.stdev(data)
print("population mean",population_mean)
print("std_deviation",std_deviation)

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df], ["average"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="MEAN"))
    fig.show()


def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data))
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

def setup():
    mean_list=[]
    for i in range(0,100):
        set_of_means=random_set_of_mean(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)

    
    mean=statistics.mean(mean_list)
    print("mean of sampeling distribution",mean)


def show_fig(mean_list):
    df=mean_list
    fig=ff.create_distplot([df],["temp"], show_hist=False)
    fig.show()

setup()

population_mean=statistics.mean(data)
print ("population_mean",population_mean)



def std_deviation():
    mean_list=[]
    for i in range(0,1000):
        set_of_means=random_set_of_mean(100)
        mean_list.append(set_of_means)
    std_deviation=statistics.stdev(mean_list)
    print ("std_deviation_of_sampeling",std_deviation)

std_deviation()