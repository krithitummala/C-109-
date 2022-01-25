import pandas as pd
import plotly.figure_factory as ff
import statistics

df = pd.read_csv("data.csv")
weightList = df["Weight"].to_list()
#fig = ff.create_distplot([df["Weight"].tolist()], ["Weight"], show_hist= False)
#fig.show()

mean = statistics.mean(weightList)
print("mean is", mean)

median = statistics.median(weightList)
print("The median is", median)

mode = statistics.mode(weightList)
print("The mode is", mode)

std_deviation = statistics.stdev(weightList)
print("The standard deviaton is", std_deviation)

std1_start, std1_end = mean - std_deviation, mean + std_deviation
std2_start, std2_end = mean -(2*std_deviation), mean +(2*std_deviation)
std3_start, std3_end = mean -(3*std_deviation), mean +(3*std_deviation)

dataInStd1 = [result for result in weightList if result>std1_start and result<std1_end]
dataInStd2 = [result for result in weightList if result>std2_start and result<std2_end]
dataInStd3 = [result for result in weightList if result>std3_start and result<std3_end]

print("{}% of data for height lies in first standard deviation".format(len(dataInStd1)*100.0/len(weightList)))
print("{}% of data for height lies in second standard deviation".format(len(dataInStd2)*100.0/len(weightList)))
print("{}% of data for height lies in third standard deviation".format(len(dataInStd3)*100.0/len(weightList)))