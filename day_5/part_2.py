freshRanges = []
ingridiance = []
isIngredance = False

def myFunc(e):
  return e[0]

with open('data.txt') as f:
    for line in f:
        row = line.strip()
        if( len( row ) == 0 ):
            isIngredance = True
            continue
        
        if( isIngredance ):
            ingridiance.append( int( row ) )
        else:
            r = row.split('-')
            freshRanges.append( (int(r[0]), int(r[1])))
        
        
        
freshCount = 0

freshRanges.sort( key=myFunc)

lastEnd = 0

for r in freshRanges:
    begin = max(r[0],lastEnd)
    print( f'begin {begin} end {r[1]} added {r[1] - begin + 1}' )
    if( r[1] < begin ):
        continue
    freshCount += r[1] - begin + 1
    lastEnd = r[1] + 1
        
print( freshCount )
            
