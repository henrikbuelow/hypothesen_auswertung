import pandas as pd

data = []


def rounded_result(result):
    """
        Rounds the result to a double with two digits after the point

        Args:
                (double) result - entered result
        Returns:
                (double) result - result with two digits after the point
        """
    result = int(result * 100)
    result = result / 100
    return result


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

    approval_rate = rounded_result(
        (column_sum[0] * 100 + column_sum[1] * 75 + column_sum[2] * 50 + column_sum[3] * 25 + column_sum[
            4] * 0) / amount_data_points)

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

    young_approval = rounded_result(
        (young_column[0] * 100 + young_column[1] * 75 + young_column[2] * 50 + young_column[3] * 25 +
         young_column[4] * 0) / young_data_points)
    adult_approval = rounded_result(
        (adult_column[0] * 100 + adult_column[1] * 75 + adult_column[2] * 50 + adult_column[3] * 25 +
         adult_column[4] * 0) / adult_data_points)
    senior_approval = rounded_result(
        (senior_column[0] * 100 + senior_column[1] * 75 + senior_column[2] * 50 + senior_column[3] * 25 +
         senior_column[4] * 0) / senior_data_points)

    young.append(young_approval)
    adult.append(adult_approval)
    senior.append(senior_approval)

"""
Ergebnisse in Textdatei schreiben
"""

high_all = []
high_young = []
high_adult = []
high_senior = []
middle_all = []
middle_young = []
middle_adult = []
middle_senior = []
low_all = []
low_young = []
low_adult = []
low_senior = []

file = open("ergebnisse.txt", "w")

file.write("Insgesamte Zustimmung zu den Hypothesen\n\n")
for index in range(0, 10):
    text = "Hypothese " + str(index + 1) + ": " + str(approval_hypothesis[index]) + "\n"
    file.write(text)
    if approval_hypothesis[index] > 62.5:
        high_all.append((index + 1))
    if 37.5 < approval_hypothesis[index] <= 62.5:
        middle_all.append((index + 1))
    if approval_hypothesis[index] <= 37.5:
        low_all.append((index + 1))

file.write("\nHypothesen mit hoher Zustimmung von allen Altersgruppen:\n")
for item in high_all:
    if item == high_all[-1]:
        file.write(str(item))
    else:
        file.write(str(item) + ', ')

file.write("\nHypothesen mit mittlerer Zustimmung von allen Altersgruppen:\n")
for item in middle_all:
    if item == middle_all[-1]:
        file.write(str(item))
    else:
        file.write(str(item) + ', ')

file.write("\nHypothesen mit niedriger Zustimmung von allen Altersgruppen:\n")
for item in low_all:
    if item == low_all[-1]:
        file.write(str(item))
    else:
        file.write(str(item) + ', ')

file.write("\n\nZustimmung der Jugendlichen zu den Hypothesen\n\n")
for index in range(0, 10):
    text = "Hypothese " + str(index + 1) + ": " + str(young[index]) + "\n"
    file.write(text)
    if young[index] > 62.5:
        high_young.append((index + 1))
    if 37.5 < young[index] <= 62.5:
        middle_young.append((index + 1))
    if young[index] <= 37.5:
        low_young.append((index + 1))

file.write("\nHypothesen mit hoher Zustimmung der Jugendlichen:\n")
for item in high_young:
    if item == high_young[-1]:
        file.write(str(item))
    else:
        file.write(str(item) + ', ')

file.write("\nHypothesen mit mittlerer Zustimmung der Jugendlichen:\n")
for item in middle_young:
    if item == middle_young[-1]:
        file.write(str(item))
    else:
        file.write(str(item) + ', ')

file.write("\nHypothesen mit niedriger Zustimmung der Jugendlichen:\n")
if len(low_young) == 0:
    file.write("/")
else:
    for item in low_young:
        if item == low_young[-1]:
            file.write(str(item))
        else:
            file.write(str(item) + ', ')

file.write("\n\nZustimmung der Erwachsenen zu den Hypothesen\n\n")
for index in range(0, 10):
    text = "Hypothese " + str(index + 1) + ": " + str(adult[index]) + "\n"
    file.write(text)
    if adult[index] > 62.5:
        high_adult.append((index + 1))
    if 37.5 < adult[index] <= 62.5:
        middle_adult.append((index + 1))
    if adult[index] <= 37.5:
        low_adult.append((index + 1))

file.write("\nHypothesen mit hoher Zustimmung der Erwachsenen:\n")
for item in high_adult:
    if item == high_adult[-1]:
        file.write(str(item))
    else:
        file.write(str(item) + ', ')

file.write("\nHypothesen mit mittlerer Zustimmung der Erwachsenen:\n")
for item in middle_adult:
    if item == middle_adult[-1]:
        file.write(str(item))
    else:
        file.write(str(item) + ', ')

file.write("\nHypothesen mit niedriger Zustimmung der Erwachsenen:\n")
for item in low_adult:
    if item == low_adult[-1]:
        file.write(str(item))
    else:
        file.write(str(item) + ', ')

file.write("\n\nZustimmung der Senioren zu den Hypothesen\n\n")
for index in range(0, 10):
    text = "Hypothese " + str(index + 1) + ": " + str(senior[index]) + "\n"
    file.write(text)
    if senior[index] > 62.5:
        high_senior.append((index + 1))
    if 37.5 < senior[index] <= 62.5:
        middle_senior.append((index + 1))
    if senior[index] <= 37.5:
        low_senior.append((index + 1))

file.write("\nHypothesen mit hoher Zustimmung der Senioren:\n")
for item in high_senior:
    if item == high_senior[-1]:
        file.write(str(item))
    else:
        file.write(str(item) + ', ')

file.write("\nHypothesen mit mittlerer Zustimmung der Senioren:\n")
for item in middle_senior:
    if item == middle_senior[-1]:
        file.write(str(item))
    else:
        file.write(str(item) + ', ')

file.write("\nHypothesen mit niedriger Zustimmung der Senioren:\n")
for item in low_senior:
    if item == low_senior[-1]:
        file.write(str(item))
    else:
        file.write(str(item) + ', ')
