import webbrowser
import data_lists as data
import csv

############DEPRECATED##############################
nV = 262

INF = 999

f = open('c://Users/alani/Documents/Maestria/2_semestre/investigacion_operaciones/Oxxo/floyd_warshall_solution.csv', 'w', newline='')
writer = csv.writer(f)

# Algorithm implementation


def floyd_warshall(G):

    distance = list(map(lambda i: list(map(lambda j: j, i)), G))

    # Adding vertices individually
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    print_solution(distance)


fw = []

# Printing the solution


def print_solution(distance):
    for i in range(nV):
        fw_row = []
        for j in range(nV):
            if distance[i][j] == INF:
                fw_row.append('inf')
                #print("INF", end=" ")
            else:
                #print(distance[i][j], end="  ")
                fw_row.append(distance[i][j])
        print(" ")
        writer.writerow(fw_row)
        fw.append(fw_row)

    f.close()


oxxo_data = data.distance_values

floyd_warshall(oxxo_data)


#n = 13334
#print(data[n])
id_list = []
min_value = 999


url_list = []
for i in range(nV):
    min_value = 999
    for j in range(nV):
        if fw[i][j] != 0 and fw[i][j] < min_value:
            min_value = fw[i][j]
            id_list.append(str(i) + ',' + str(j))

    short_path = id_list[-1]
    index = short_path.split(',')
    print(int(index[1]))

    url_item = "https://www.google.com.mx/maps/dir/" + data.coordinates[i] + "/" + data.coordinates[int(index[1])]

    url_list.append(url_item)


# url = "https://www.google.com.mx/maps/dir/" + data[n][0] + "/" + data[n][1]

print(url_list)


#for i in range(5):
    #webbrowser.open(url_list[i])

coord_ordered = []
url_head = 'https://www.google.com.mx/maps/dir/'

url = ''
path_data = []
n = 0

for i in data.coordinates:

    url = url + i + '/'

    n = n + 1

    if n == 10:
        path_data.append(url_head + url)
        print(url_head+url)
        n = 0
        url = ''


print(path_data[0])
# webbrowser.open(path_data[0])