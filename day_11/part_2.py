from functools import reduce
def countPaths( ordered, graph, start, end):
    path = dict()
    for item in ordered:
        path[item] = 0

    path[end] = 1

    for item in ordered:
        for edge in devices[item]:
            path[item] += path[edge]

    return(path[start])


def toposort(data):
    result = []
    for k, v in data.items():
        v.discard(k) # Ignore self dependencies
    extra_items_in_deps = reduce(set.union, data.values()) - set(data.keys())
    data.update({item:set() for item in extra_items_in_deps})
    while True:
        ordered = set(item for item,dep in data.items() if not dep)
        if not ordered:
            break
        result =  result + sorted(ordered)
        data = {item: (dep - ordered) for item,dep in data.items()
                if item not in ordered}
    return result


devices = dict()
with open('data.txt') as f:
    for line in f:
        l = line.strip().split()
        connection = set()
        for con in l[1:]:
            connection.add(con)
        devices[l[0][:-1]] = connection

outCount = 0
start = 'svr'
end = 'out'
dac = 'dac'
fft = 'fft'

ordered = toposort(devices)

result = countPaths(ordered, devices, start, dac) * countPaths(ordered, devices, dac, fft) * countPaths(ordered, devices, fft, end)
result += countPaths(ordered, devices, start, fft) * countPaths(ordered, devices, fft, dac) * countPaths(ordered, devices, dac, end)


print(result)

