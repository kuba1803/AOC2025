rows = []

with open('data.txt') as f:
    for line in f:
        rows.append( list(line.strip()) )

result = 0
changed = True
while changed:
    changed = False
    for y in range( len(rows) ):
        print(rows[y])
        for x in range( len( rows[y] ) ):
            if( rows[y][x]!='@'):
                continue

            adjust = 0
            for i in ( -1, 0, 1 ):
                ayIdx = y + i
                if( ayIdx < 0 or ayIdx >= len(rows)):
                    continue

                for j in ( -1, 0, 1 ):
                    axIdx = x + j
                    if (axIdx < 0 or axIdx >= len(rows)):
                        continue

                    if( i == 0 and j == 0):
                        continue

                    if( rows[ayIdx][axIdx]=='@' or rows[ayIdx][axIdx]=='x'):
                        adjust += 1

            print( f'y {y} x {x} : adjust {adjust}')
            if( adjust < 4):
                rows[y][x] = 'x'
                result+=1

    for y in range( len(rows) ):
        print(rows[y])
        for x in range(len(rows[y])):
            if( rows[y][x]=='x' ):
                changed = True
                rows[y][x] = '.'



print(result)