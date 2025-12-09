def sortFunc(e):
    return e[0]

distances = []
junction = []

idx = 0
with open('example.txt') as f:
    for line in f:
        junction.append(list(map(int,line.strip().split(","))))

directConnection = []

for y in range(len(junction)):
    directConnection.append(set([y]))
    for x in range(y,len(junction)):
        if( y != x):
            distance = ((junction[y][0]-junction[x][0])**2 + (junction[y][1]-junction[x][1])**2 + (junction[y][2]-junction[x][2])**2)**(1/2)
            distances.append((distance,x,y))
            
distances.sort(key=sortFunc, reverse=True)


print(distances[0])
print(distances[1])
#print(directConnection)

while True:
    if( len(distances)==0 ):
        break
    
    (minDistance,minX,minY) = distances.pop()


    print(f'idx {minX} x {junction[minX]} idy {minY} y {junction[minY]} minDistance {minDistance}')
    connection = directConnection[minY] | directConnection[minX]
    for idx in connection:
        directConnection[idx] = connection

    directConnection[minX] = directConnection[minY]
    
    if( len(directConnection[minY]) == len(junction) ):
        result = junction[minY][0] * junction[minX][0]
        print( f'idx {minX} minX {junction[minX]} idy {minY} minY {junction[minY]}')
        break


print(result)
