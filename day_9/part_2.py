points = []
lines = []
with open('data.txt') as f:
    for line in f:
        points.append(list(map(int, line.strip().split(","))))

for idx in range(len(points)):
    lines.append((points[idx],points[idx - 1]))
print(points)
print(lines)
maxArea = 0

for y in range(len(points)):
    for x in range(y + 1, len(points)):
        area = (abs(points[y][0] - points[x][0]) + 1) * (abs(points[y][1] - points[x][1]) + 1)
        print(f'x {points[x]}  y {points[y]} area {area}')

        if (area < maxArea):
            continue

        use = True
        for l in lines:
            print(l)
            if (l[0][0] == l[1][0]
                    and l[0][0] < max(points[x][0], points[y][0])
                    and l[0][0] > min(points[x][0], points[y][0])):
                if (max(l[0][1], l[1][1]) > min(points[x][1], points[y][1])
                        and min(l[0][1], l[1][1]) < max(points[x][1], points[y][1])):
                    #print(f'p {l} rejected')
                    use = False
                    break

            if (l[0][1] == l[1][1]
                    and l[0][1] < max(points[x][1], points[y][1])
                    and l[0][1] > min(points[x][1], points[y][1])):
                if (max(l[0][0], l[1][0]) > min(points[x][0], points[y][0])
                        and min(l[0][0], l[1][0]) < max(points[x][0], points[y][0])):
                    #print(f'p {l} rejected')
                    use = False
                    break

        #print(f'upLeft {upLeft} downRigth {downRigth} area {area} use {use}')
        if (use):
            maxArea = area

print(points)
print(maxArea)
