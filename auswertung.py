import pandas as pd
import numpy as np
data = []

"""
read all csv files with data from hypothesis into  data list
"""
for index in range(0, 10):
    name = 'hypothese' + str(index + 1) + '.CSV'
    #print(name)
    data.append(pd.read_csv(name, sep=";"))
    #print(data[index])

"""
Calculating the approval rating for each hypothesis without consideration of age
"""
approval_hypothesis =[]
column_names = ['Stimme voll zu', 'Stimme eher zu', 'Neutral', 'Stimme eher nicht zu', 'Stimme nicht zu']

for index in range(0, 10):
        relevant_file = data[index]
        column_sum = []
        amount_data_points = 0

        for names in column_names:
                relevant_column = relevant_file[names]
                column_sum.append(relevant_column.sum())
                amount_data_points += relevant_column.sum()

        approval_rate = (column_sum[0] * 100 + column_sum[1] * 75 + column_sum[2] * 50 + column_sum[3] * 25 + column_sum[4] * 0) / amount_data_points
        approval_hypothesis.append(approval_rate)

for hypothesis in approval_hypothesis:
        print(str(hypothesis))


