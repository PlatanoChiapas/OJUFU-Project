import csv


# Main Purpose: This code reads csv files containing the OXXO distances data and creates
# a new csv file with fuzzy data, merging the data from the morning, afternoon and night periods.


# time_select(time_list)
# def time_select(time_list):
# if len(time_list) > 1:
# time_list = time_list[-2:]
# else:
# time_list = time_list[0]
# print(time_list)
# time_list_strip = time_list.strip('-')
# print(time_list_strip)

# return time_list_strip

number_nodes = 262


def csv_to_list(key_file):
    # Opens the file that contains the coordinates for each location
    save_path = "data/csv_data/distance_data_" + key_file + ".csv"
    print(save_path)
    file_distance_data = open(save_path, 'r')

    data_raw = file_distance_data.read()  # Reads the csv containing the coordinates list

    data_raw = data_raw.split()  # Separates the csv file by whitespaces and creates a new line for each element

    distance_data = []

    for line in data_raw:
        row = line.split(',')
        row_values = []
        for val in row:
            row_values.append(val)

        distance_data.append(row_values)

    file_distance_data.close()
    return distance_data


distance_data_morning = csv_to_list("1_morning")
distance_data_afternoon = csv_to_list("2_afternoon")
distance_data_night = csv_to_list("3_night")

fuzzy_distance_data = []
# fuzzy_morning_distance_data = []
# fuzzy_afternoon_distance_data = []
# fuzzy_evening_distance_data = []


fuzzy_file = open('data/fuzzy_distance_data.csv', 'w', newline='')

writer = csv.writer(fuzzy_file)

for i in range(number_nodes):
    fuzzy_distance_data_row = []
    # fuzzy_morning_distance_data_row = []
    # fuzzy_afternoon_distance_data_row = []
    # fuzzy_evening_distance_data_row = []
    for j in range(number_nodes):
            
        fuzzy_distance_value = distance_data_morning[i][j] + '--' + \
                                distance_data_afternoon[i][j] + '--' + \
                                distance_data_night[i][j]

        # time_morning = time_select(time_morning)
        # time_afternoon = time_select(time_afternoon)
        # time_evening = time_select(time_evening)
        try:
            fuzzy_distance_data_row.append(fuzzy_distance_value)
        except "INVALID DATA":
            print("Fuzzyfication failed")

    fuzzy_distance_data.append(fuzzy_distance_data_row)

    writer.writerow(fuzzy_distance_data_row)

fuzzy_file.close()

print(fuzzy_distance_data)

