import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import pandas as pd
import random

df= pd.read_csv("data.csv")
data=df["url"].tolist()

def random_set_of_mean(counter):
    dataSet=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data))
        value=data[random_index]
        dataSet.append(value)
    mean=statistics.mean(dataSet)
    return mean

def show_fig(mean_list):
    df=mean_list
    mean=statistics.mean(mean_list)
    print(mean)
    fig=ff.create_distplot([df],["url"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="mean"))
    fig.show()


def setUp():
    mean_list=[]
    for i in range(0,100):
        set_of_mean=random_set_of_mean(30)
        mean_list.append(set_of_mean)
    show_fig(mean_list)
setUp()
