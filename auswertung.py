import pandas as pd

data = []

"""
read all csv files with data from hypothesis into  data list
"""
for index in range(0, 10):
    name = 'hypothese' + str(index + 1) + '.CSV'
    data.append(pd.read_csv(name, sep=";"))

"""
Calculating the approval rating for each hypothesis without consideration of age
"""
approval_hypothesis = []
column_names = ['Stimme voll zu', 'Stimme eher zu', 'Neutral', 'Stimme eher nicht zu', 'Stimme nicht zu']

for index in range(0, 10):
    relevant_file = data[index]
    column_sum = []
    amount_data_points = 0

    for names in column_names:
        relevant_column = relevant_file[names]
        column_sum.append(relevant_column.sum())
        amount_data_points += relevant_column.sum()

    approval_rate = (column_sum[0] * 100 + column_sum[1] * 75 + column_sum[2] * 50 + column_sum[3] * 25 + column_sum[
        4] * 0) / amount_data_points
    approval_hypothesis.append(approval_rate)

"""
Calculating the approval rating for each hypothesis with consideration of age
"""
young = []
adult = []
senior = []

for index in range(0, 10):
        relevant_file = data[index]

        young_column = []
        adult_column = []
        senior_column = []

        young_data_points = 0
        adult_data_points = 0
        senior_data_points = 0

        for names in column_names:

                relevant_column = relevant_file[names]

                young_column.append(relevant_column[0])
                young_data_points += relevant_column[0]

                adult_column.append(relevant_column[1])
                adult_data_points += relevant_column[1]

                senior_column.append(relevant_column[2])
                senior_data_points += relevant_column[2]

        young_approval = (young_column[0] * 100 + young_column[1] * 75 + young_column[2] * 50 + young_column[3] * 25 +
                          young_column[4] * 0) / young_data_points
        adult_approval = (adult_column[0] * 100 + adult_column[1] * 75 + adult_column[2] * 50 + adult_column[3] * 25 +
                          adult_column[4] * 0) / adult_data_points
        senior_approval = (senior_column[0] * 100 + senior_column[1] * 75 + senior_column[2] * 50 + senior_column[3] * 25 +
                          senior_column[4] * 0) / senior_data_points

        young.append(young_approval)
        adult.append(adult_approval)
        senior.append(senior_approval)

"""
Printing the results to the consol
"""

print('Zustimmung zu den Hypothesen insgesamt:', approval_hypothesis)
print('Zustimmung der Jugendlichen zu den Hypothesen:', young)
print('Zustimmung der Erwachsenen zu den Hypothesen:',  adult)
print('Zustimmung der Senioren zu den Hypothesen:', senior)

