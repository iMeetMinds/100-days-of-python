import pandas

data = pandas.read_csv("./2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

squiral_gray_count = len(data[data['Primary Fur Color'] == 'Gray'])
squiral_black_count = len(data[data['Primary Fur Color'] == 'Black'])
squiral_red_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])

data_dict = {
    "Fur Color" : ["Gray", "Red", "Black"],
    "Count" : [ squiral_gray_count, squiral_red_count, squiral_black_count ]
}

count_data = pandas.DataFrame(data_dict)
print(count_data)

count_data.to_csv("squiral_count.csv")



