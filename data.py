import csv
import random
import statistics
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("sample_2.csv")
data = df["reading_time"].tolist()

#fig = ff.create_distplot([data], ["Math_score"],show_hist=False)
#fig.show()
pmean = statistics.mean(data)
pstd_dev = statistics.stdev(data)
print("The z score is =", pmean)
print("std dev of sampling distrubition", pstd_dev)

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value= data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list=[]
for i in range (0,1000):
    set_of_mean = random_set_of_mean(100)
    mean_list.append(set_of_mean)

std_dev =statistics.stdev(mean_list)
mean =  statistics.mean(mean_list)
print("mean of sampling distribbution ", mean)

std_1s,std_1e=mean-std_dev,mean+std_dev
std_2s,std_2e=mean-(2*std_dev),mean+(2*std_dev)
std_3s,std_3e=mean-(3*std_dev),mean+(3*std_dev)
fig = ff.create_distplot([mean_list], ["studentMark"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.20],mode="lines", name="mean"))
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[std_1s,std_1s],y=[0,0.17],mode="lines",name="std_dev"))
fig.add_trace(go.Scatter(x=[std_1e,std_1e],y=[0,0.17],mode="lines",name="std_dev"))
fig.add_trace(go.Scatter(x=[std_2s,std_2s],y=[0,0.17],mode="lines",name="std_dev2"))
fig.add_trace(go.Scatter(x=[std_2e,std_2e],y=[0,0.17],mode="lines",name="std_dev2"))
fig.show()

df = pd.read_csv("sample_2.csv")
data = df ["reading_time"].tolist()
 
mean_of_sample1 = statistics.mean(data)
print("mean_of_sample1", mean_of_sample1)
fig = ff.create_distplot([mean_list],["studentmarks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[mean_of_sample1,mean_of_sample1],y=[0,0.17],mode="lines",name="mean_of_sample1"))
fig.add_trace(go.Scatter(x=[std_1e,std_1e],y=[0,0.17],mode="lines",name="std1_end"))
fig.add_trace(go.Scatter(x=[std_2e,std_2e],y=[0,0.17],mode="lines",name="std2_end"))
fig.show()