import json
graph = [
    [0,1,1,1,0,0,0],
    [1,0,0,0,1,0,0],
    [1,0,0,1,0,0,0],
    [1,0,1,0,1,0,0],
    [0,1,0,1,0,1,1],
    [0,0,1,0,1,0,1],
    [0,0,0,0,1,1,0]
]

graph_dict = {
    0 : [1,2,3],
    1 : [0,4],
    2 : [0,3],
    3 : [0,2,4],
    4 : [1,3,5,6],
    5 : [2,4,6],
    6 : [4,5]
}

def json_file(graph):
    file = 'graph.json'
    with open(file, 'w') as f:
        json.dump(graph, f)

def iterate_graph(graph_dict):
    connection_list = []
    for k,v in graph_dict.items():
        for i in v:
            con = '{0}-{1}'.format(k, i)
            connection_list.append(con)
    return connection_list


print(iterate_graph(graph_dict))

json_file(graph_dict)

