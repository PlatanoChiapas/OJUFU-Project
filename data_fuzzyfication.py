import csv


def time_select(time_list):
    if len(time_list) > 1:
        time_list = time_list[-2:]
    else:
        time_list = time_list[0]
    # print(time_list)
    time_list_strip = time_list.strip('-')
    # print(time_list_strip)

    return time_list_strip


def csv_to_list(n_set):
    # Opens the file that contains the coordinates for each location
    save_path = "c://Users/alani/Documents/Maestria/2_semestre/investigacion_operaciones/fuzzy/data_25x25/data" \
                "/time_set_25x25" + str(n_set) + ".csv "
    print(save_path)
    file_time_data = open(save_path, 'r')

    data_raw = file_time_data.read()  # Reads the csv containing the coordinates list

    data_raw = data_raw.split()  # Separates the csv file by whitespaces and creates a new line for each element

    time_data = []

    for line in data_raw:
        row = line.split(',')
        row_values = []
        for val in row:
            row_values.append(val)

        time_data.append(row_values)

    file_time_data.close()
    return time_data


time_data_1 = csv_to_list(-1)
time_data_4 = csv_to_list(-4)
time_data_6 = csv_to_list(-6)

fuzzy_time_data = []
fuzzy_morning_time_data = []
fuzzy_afternoon_time_data = []
fuzzy_evening_time_data = []


fuzzy_file = open('fuzzy_data_25x25-1-4-6.csv', 'w', newline='')

writer = csv.writer(fuzzy_file)

for i in range(25):
    fuzzy_time_data_row = []
    fuzzy_morning_time_data_row = []
    fuzzy_afternoon_time_data_row = []
    fuzzy_evening_time_data_row = []
    for j in range(25):

        time_morning = time_data_1[i][j][-3:]
        time_afternoon = time_data_4[i][j][-3:]
        time_evening = time_data_6[i][j][-3:]

        time_morning = time_select(time_morning)
        time_afternoon = time_select(time_afternoon)
        time_evening = time_select(time_evening)

        if time_morning == time_afternoon == time_evening:
            fuzzy_time = time_morning
        else:
            fuzzy_time = time_morning + '-' + time_afternoon + '-' + time_evening

        fuzzy_time_data_row.append(fuzzy_time)
        try:
            fuzzy_morning_time_data_row.append(float(time_morning))
            fuzzy_afternoon_time_data_row.append(float(time_afternoon))
            fuzzy_evening_time_data_row.append(float(time_evening))
        except:
            fuzzy_morning_time_data_row.append(0.0)
            fuzzy_afternoon_time_data_row.append(0.0)
            fuzzy_evening_time_data_row.append(0.0)

    fuzzy_time_data.append(fuzzy_time_data_row)
    fuzzy_morning_time_data.append(fuzzy_morning_time_data_row)
    fuzzy_afternoon_time_data.append(fuzzy_afternoon_time_data_row)
    fuzzy_evening_time_data.append(fuzzy_evening_time_data_row)

    writer.writerow(fuzzy_time_data_row)

fuzzy_file.close()
print(fuzzy_time_data)
print(fuzzy_morning_time_data)
print(fuzzy_afternoon_time_data)
print(fuzzy_evening_time_data)
