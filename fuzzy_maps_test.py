import fuzzy_floyd_warshall as fwt
import webbrowser


def optimal_map_path(fw):

    cost_data = fw
    start = 0
    final_path = [start]
    actual_coord = 0
    for n in range(fwt.nV):
        next_coord = actual_coord
        min_value = 999
        id_list = []

        for j in range(fwt.nV):
            if cost_data[next_coord][j] != 0 and cost_data[next_coord][j] < min_value:
                min_value = cost_data[next_coord][j]
                id_list.append(j)

        minor_cost = id_list[-1]
        final_path.append(minor_cost)
        # print(minor_cost)

        for n in range(fwt.nV):
            cost_data[n][minor_cost] = 100

        actual_coord = minor_cost

    print(final_path)

    # url_item = "https://www.google.com.mx/maps/dir/" + fwt.data.coordinates[i] + "/" + fwt.data.coordinates[int(index[1])]

    # url_list.append(url_item)

    # url = "https://www.google.com.mx/maps/dir/" + data[n][0] + "/" + data[n][1]

    # print(url_list)

    # for i in range(5):
    # webbrowser.open(url_list[i])

    # coord_ordered = []
    url_head = 'https://www.google.com.mx/maps/dir/'

    url = ''
    optimal_path = []
    n = 0

    for i in final_path:

        url = url + fwt.data.coordinates[i] + '/'

        n = n + 1

        if n == 10:
            optimal_path.append(url_head + url)
            # print(url_head+url)
            n = 0
            url = ''

    print('Optimal path: ', optimal_path[0])
    #webbrowser.open(optimal_path[0])


optimal_map_path(fwt.fw_morning)
optimal_map_path(fwt.fw_afternoon)
optimal_map_path(fwt.fw_evening)
