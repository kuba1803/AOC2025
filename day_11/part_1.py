devices = dict()
with open('data.txt') as f:
    for line in f:
        l = line.strip().split()
        connection = []
        for con in l[1:]:
            connection.append(con)
        devices[l[0][:-1]] = connection

outCount =0
queue = ['you']

while len(queue)>0:
    device = queue.pop(0)
    for node in devices[device]:
        if( node == "out"):
            outCount += 1
        else:
            queue.append(node)






print(outCount)

