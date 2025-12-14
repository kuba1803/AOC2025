points = []
line = []
with open('example.txt.txt') as f:
    for line in f:
        points.append(list(map(int,line.strip().split(","))))

print(points)

maxArea = 0

for y in range(len(points)):
    for x in range(y+1,len(points)):
        area = (abs(points[y][0] - points[x][0])+1) * (abs(points[y][1] - points[x][1])+1)
        print( f'x {points[x]}  y {points[y]} area {area}')

        if( area < maxArea ):
            continue

        maxArea = area




print(points)
print(maxArea)