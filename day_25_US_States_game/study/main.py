# with open('weather_data.csv') as f:
#     data = f.readlines()
# print(data)

# import csv
#
# with open('weather_data.csv') as f:
#     data = csv.reader(f)
#     temperatures = []
#     for row in data:
#         temp = row[1]
#         if temp.isdigit():
#             temperatures.append(temp)
# print(temperatures)

import pandas

# data = pandas.read_csv('weather_data.csv')
# # data_dict = data.to_dict()
# # print(data_dict)
#
# temp_list = data['temp'].to_list()
# # print(temp_list)
# # average = sum(temp_list) / len(temp_list)
# # print(round(average, 1))
# temps = data['temp']
# print(temps)
# average = temps.mean()
# print('average', round(average, 1))
# print('min', temps.min(), '\nmax', temps.max())
#
# # Get data in colomns
# print(data['condition'])
# print(data.condition)
# print(data.day)
#
# # Get data in rows
# print(data[data.day == 'Monday'])
#
# # Max temp row
# print(data[data.temp == data.temp.max()])
#
# def cel_fah(n, to_fah=True):
#     if to_fah:
#         return n * 9 / 5 + 32
#     return (n - 32) * 5 / 9
#
# monday = data[data.day == 'Monday']
# print(monday.condition)
# mon_temp = monday.temp
# print(cel_fah(mon_temp))
#
# # Create dataframe from scratch
# data_dict = {
#     'students': ['Amy', 'James', 'Angela'],
#     'scores': [76, 56, 65],
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv('students.csv')

data = pandas.read_csv('Squirrel_Data.csv')
# gray = data[data['Primary Fur Color'] == 'Gray']
# red = data[data['Primary Fur Color'] == 'Cinnamon']
# black = data[data['Primary Fur Color'] == 'Black']
# data_dict = {
#     'Fur Color': ['gray', 'red', 'black'],
#     'Count': [len(gray), len(red), len(black)],
# }
colors = list(set(data['Primary Fur Color'].to_list()))
counts = []
colors2 = list(colors)
for color in colors2:
    if type(color) == str:
        counts.append(len(data[data['Primary Fur Color'] == color]))
    else:
        colors.remove(color)
data_dict = {
    'Fur Color': colors,
    'Count': counts,
}
print(colors, counts)
df = pandas.DataFrame(data_dict)
df.to_csv('squirrel_count.csv')
