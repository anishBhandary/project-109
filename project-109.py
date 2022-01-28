import plotly.figure_factory as ff
import pandas as pd
import statistics

df = pd.read_csv("data1.csv")
reading_score_list = df["reading score"].to_list()
reading_score_mean = statistics.mean(reading_score_list)
reading_score_median = statistics.median(reading_score_list)
reading_score_mode = statistics.mode(reading_score_list)
reading_score_stdDeviation = statistics.stdev(reading_score_list)

reading_score_first_std_Deviation_start,reading_score_first_std_Deviation_end = (reading_score_mean - reading_score_stdDeviation),reading_score_mean + reading_score_stdDeviation
reading_score_sec_std_Deviation_start,reading_score_sec_std_Deviation_end = reading_score_mean - (2*reading_score_stdDeviation),reading_score_mean + (2*reading_score_stdDeviation)
reading_score_third_std_Deviation_start,reading_score_third_std_Deviation_end = reading_score_mean - (3*reading_score_stdDeviation),reading_score_mean + (3*reading_score_stdDeviation)

reading_score_list_data_within_first_Deviation = [result for result in reading_score_list if result > reading_score_first_std_Deviation_start and result < reading_score_first_std_Deviation_end]
reading_score_list_data_within_sec_Deviation = [result for result in reading_score_list if result > reading_score_sec_std_Deviation_start and result < reading_score_sec_std_Deviation_end]
reading_score_list_data_within_third_Deviation = [result for result in reading_score_list if result > reading_score_third_std_Deviation_start and result < reading_score_third_std_Deviation_end]

print("Mean Median Mode of reading_score is {},{},{} respectively".format(reading_score_mean,reading_score_median,reading_score_mode))
print("{} % of data lies between first Standard Deviation".format(len(reading_score_list_data_within_first_Deviation)*100.0/len(reading_score_list)))
print("{} % of data lies between sec Standard Deviation".format(len(reading_score_list_data_within_sec_Deviation)*100.0/len(reading_score_list)))
print("{} % of data lies between third Standard Deviation".format(len(reading_score_list_data_within_third_Deviation)*100.0/len(reading_score_list)))
