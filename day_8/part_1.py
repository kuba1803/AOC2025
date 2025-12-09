def sortFunc(e):
    return len(e)

distances = []
junction = []

idx = 0
with open('data.txt') as f:
    for line in f:
        junction.append(list(map(int,line.strip().split(","))))

directConnection = []

for y in range(len(junction)):
    distances.append([0]*len(junction))
    directConnection.append([y])
    for x in range(len(junction)):
        if( y == x):
            distances[y][x] = 0
        else:
            distance = ((junction[y][0]-junction[x][0])**2 + (junction[y][1]-junction[x][1])**2 + (junction[y][2]-junction[x][2])**2)**(1/2)
            distances[y][x] = distance

print(directConnection)

for run in range(1000):
    minDistance = 999999999999
    minY = -1
    minX = -1

    for y in range(len(distances)):
        #print(distances[y])
        for x in range(y+1,len(distances)):
            if( distances[y][x]>0 and distances[y][x]<minDistance):
                #print(f'x = {x} y = {y} distance {distances[y][x]}')
                minX=x
                minY=y
                minDistance = distances[y][x]

    #print( f'minX {minX} minY {minY}')
    if(minY==-1 and minX==-1):
        break

    #print(f'x {junction[minX]} y {junction[minY]}')
    distances[minY][minX] = 0
    directConnection[minY].append(minX)
    distances[minX][minY] = 0
    directConnection[minX].append(minY)


circuit = []
visited = [False]* len(directConnection)
stack = []
for d in range(len(directConnection)):
    if( visited[d] ):
        continue
    stack.append(d)
    circuit.append([])
    while len(stack)>0:
        idx = stack.pop()
        if( visited[idx] ):
            continue

        visited[idx] = True
        circuit[len(circuit)-1].append(idx)
        for i in directConnection[idx]:
            stack.append(i)

circuit.sort(key=sortFunc, reverse=True)

result = 1
for i in range(3):
    result*=len(circuit[i])
    print(circuit[i])

print(result)









