from day_6.part_1 import result

rows = []
matrix = []

with open('data.txt') as f:
    for line in f:
        rows.append( list(line.strip()))
        matrix.append( [0]*len(line.strip()))

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

    print(rows[y])

result = 0
for x in range(len(rows[len(rows)-1])):
    if( rows[len(rows)-1][x]=="|"):
        matrix[len(rows)-1][x] = 1

for y in range(len(rows)-2,-1,-1):
    for x in range(len(rows[y])):
        if(rows[y][x]=="|" or rows[y][x]=="S"):
            matrix[y][x] = matrix[y+1][x]

        if( rows[y][x]=="S" ):
            result = matrix[y+1][x]

    for x in range(len(rows[y])):
        if(rows[y][x]=="^"):
            matrix[y][x]= matrix[y][x+1] + matrix[y][x-1]

print(result)
