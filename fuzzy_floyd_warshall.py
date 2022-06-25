import webbrowser
import data_lists as data
import csv
import data_fuzzyfication as fuzzy_data

nV = 25

INF = 999

# f = open('c://Users/alani/Documents/Maestria/2_semestre/investigacion_operaciones/Oxxo/floyd_warshall_solution.csv
# ', 'w', newline='')
# f_morning = open('fuzzy_morning_floyd_warshall_solution.csv', 'w', newline='')
# f_afternoon = open('fuzzy_afternoon_floyd_warshall_solution.csv', 'w', newline='')
# f_evening = open('fuzzy_evening_floyd_warshall_solution.csv', 'w', newline='')
fuzzy_file = open('fuzzy_floyd_warshall_solution.csv', 'w', newline='')

# writer_morning = csv.writer(f_morning)
# writer_afternoon = csv.writer(f_afternoon)
# writer_evening = csv.writer(f_evening)
writer_fuzzy = csv.writer(fuzzy_file)


# Algorithm implementation


def print_solution(distance, fw_row):
    fw = []

    for i in range(nV):
        fw_row.clear()
        for j in range(nV):
            if distance[i][j] == INF:
                fw_row.append('inf')
                # print("INF", end=" ")
            else:
                # print(distance[i][j], end="  ")
                fw_row.append(distance[i][j])

        writer_fuzzy.writerow(fw_row)
        # if day_phase == 'm':
        # writer_morning.writerow(fw_row)
        # fw.append(fw_row)
        # elif day_phase == 'a':
        # writer_afternoon.writerow(fw_row)
        # fw.append(fw_row)
        # elif day_phase == 'e':
        # writer_evening.writerow(fw_row)
        # fw.append(fw_row)
    fuzzy_file.close()
    # if day_phase == 'm':
    # f_morning.close()
    # if day_phase == 'a':
    # f_afternoon.close()
    # if day_phase == 'e':
    # f_evening.close()
    print('first_solution', fw)
    return fw


def floyd_warshall(g, day_phase, fw_row):
    distance = list(map(lambda i: list(map(lambda j: j, i)), g))

    # Adding vertices individually
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    fw = print_solution(distance, fw_row)

    return fw


# Printing the solution


def map_route_generator(fw):
    print('Solution: ', fw)
    id_list = []
    index_route = [0]
    # min_value = 999

    url_list = []
    for i in range(nV):
        min_value = 999
        for j in range(nV):
            if fw[i][j] != 0 and fw[i][j] < min_value:
                min_value = fw[i][j]
                id_list.append(str(i) + ',' + str(j))

        short_path = id_list[-1]
        index = short_path.split(',')
        # print(int(index[1]))

        url_item = "https://www.google.com.mx/maps/dir/" + data.coordinates[i] + "/" + data.coordinates[int(index[1])]
        index_route.append(int(index[1]))
        url_list.append(url_item)
    print('index', index_route)
    # url = "https://www.google.com.mx/maps/dir/" + data[n][0] + "/" + data[n][1]

    # print(url_list)

    # for i in range(5):
    # webbrowser.open(url_list[i])

    # coord_ordered = []
    url_head = 'https://www.google.com.mx/maps/dir/'

    url = ''
    path_data = []
    n = 0

    for i in range(25):

        url = url + data.coordinates[index_route[i]] + '/'

        n = n + 1

        if n == 10:
            path_data.append(url_head + url)
            # print(url_head + url)
            n = 0
            url = ''

    # print(path_data[0])
    # webbrowser.open(path_data[0])


oxxo_data = data.distance_values
fuzzy_oxxo_data = fuzzy_data.fuzzy_time_data
fuzzy_morning_data = fuzzy_data.fuzzy_morning_time_data
fuzzy_afternoon_data = fuzzy_data.fuzzy_afternoon_time_data
fuzzy_evening_data = fuzzy_data.fuzzy_evening_time_data

fw_morning_row = []
fw_afternoon_row = []
fw_evening_row = []
# floyd_warshall(oxxo_data)
fw_morning = floyd_warshall(fuzzy_morning_data, 'm', fw_morning_row)
fw_afternoon = floyd_warshall(fuzzy_afternoon_data, 'a', fw_afternoon_row)
fw_evening = floyd_warshall(fuzzy_evening_data, 'e', fw_evening_row)

map_route_generator(fw_morning)
map_route_generator(fw_afternoon)
map_route_generator(fw_evening)
