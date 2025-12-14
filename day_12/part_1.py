
presents = []
regions = []
lastID = 0


maxResult = 0
minResult = 0
with open('data.txt') as f:
    for line in f:
        if( ":" in line ):
            if( "x" in line ):
                l = line.strip().split(":")
                dimention = list(map(int, l[0].strip().split("x")))
                area = dimention[0]*dimention[1]

                minimalRequiredSpace = 0
                maximalRequiredSpace = 0
                presentList = list(map(int, l[1].strip().split()))
                for p in range(len(presentList)):
                    minimalRequiredSpace += presents[p] * presentList[p]
                    maximalRequiredSpace += 9 * presentList[p]

                print( f' available area {area} minimal required space {minimalRequiredSpace} maximalRequiredSpace {maximalRequiredSpace}' )
                if(minimalRequiredSpace <= area):
                    maxResult += 1

                if (maximalRequiredSpace <= area):
                    minResult += 1

            else:
                lastID = int(line.strip().split(":")[0])
        else:
            if( len(line) > 0 ):
                if( lastID == len(presents) ):
                    presents.append(0)
                presents[lastID] += line.count("#")



print( f'maxResult {maxResult}' )
print( f'minResult {minResult}' )


