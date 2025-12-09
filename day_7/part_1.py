rows = []

with open('data.txt') as f:
    for line in f:
        rows.append( list(line.strip()))

count = 0
for y in range(1,len(rows)):
    for x in range(len(rows[y])):
        if(  rows[y][x]=="." ):
            if( rows[y-1][x]=="|" or rows[y-1][x]=="S"):
                rows[y][x]="|"
        elif(  rows[y][x]=="^" ):
            if( rows[y-1][x]=="|" or rows[y-1][x]=="S"):
                rows[y][x + 1] = "|"
                rows[y][x - 1] = "|"
                count += 1

    print(rows[y])

print(count)


