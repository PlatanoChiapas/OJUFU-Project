import webbrowser
import data_lists as data
import csv


nV = 262

INF = 999

f = open('c://Users/alani/Documents/Maestria/2_semestre/investigacion_operaciones/Oxxo/floyd_warshall_solution.csv', 'w', newline='')
writer = csv.writer(f)

f_path = open('c://Users/alani/Documents/Maestria/2_semestre/investigacion_operaciones/Oxxo/floyd_warshall_paths.csv', 'w', newline='')
writer_path = csv.writer(f_path)

# Algorithm implementation


def floyd_warshall(G):

    distance = list(map(lambda i: list(map(lambda j: j, i)), G))
    #paths = list(map(lambda i: list(map(lambda j: j, i)), G))
    # Adding vertices individually
    index_i = 0
    index_j = 0
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
                #paths[i][j] = j
                index_i = i
                index_j = j
    print_solution(distance)



fw = []
path_data = []
# Printing the solution


def print_solution(distance):
    for i in range(nV):
        fw_row = []
        path_row = []
        for j in range(nV):
            if distance[i][j] == INF:
                #print("INF", end=" ")
                fw_row.append('INF')
            else:
                #print(distance[i][j], end="  ")
                fw_row.append(distance[i][j])
                #path_row.append(index_j+1)
        #print(" ")
        writer.writerow(fw_row)
        fw.append(fw_row)

        writer_path.writerow(path_row)
        #path_data.append(path_row)

    f.close()


oxxo_data = data.distance_values

floyd_warshall(oxxo_data)


#n = 13334
#print(data[n])


