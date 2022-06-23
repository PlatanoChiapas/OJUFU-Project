import webbrowser
import data_lists as data

nV = 262 * 262

INF = 999


# Algorithm implementation
def floyd_warshall(G):
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))

    # Adding vertices individually
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    print_solution(distance)


# Printing the solution
def print_solution(distance):
    for i in range(nV):
        for j in range(nV):
            if(distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")


G = data.distance_values

floyd_warshall(G)

#n = 13334
#print(data[n])

#url = "https://www.google.com.mx/maps/dir/" + data[n][0] + "/" + data[n][1]

#webbrowser.open(url)