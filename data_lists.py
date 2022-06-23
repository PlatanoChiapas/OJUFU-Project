import webbrowser

file_coord = open("oxxo_coordinates.csv", 'r')

coord_list = file_coord.read()

coord_list = coord_list.split()

coordinates = []


for line in coord_list:
    line = line.strip('"')
    coordinates.append(line)

file = open("distance_values.csv", 'r')

distances = file.read()

distances = distances.split()


distance_values = []

for line in distances:
    row = line.split(',')
    row_values = []
    for val in row:
        row_values.append(float(val))

    distance_values.append(row_values)


new_row = []


i = 0
j = 0
data = []

for row in distance_values:
    j = 0
    for val in distance_values[j]:

        data_row = [coordinates[i], coordinates[j], distance_values[i][j]]
        # print('row: ', data_row)
        data.append(data_row)

        j = j + 1
    i = i + 1
