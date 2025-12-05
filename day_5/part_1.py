freshRanges = []
ingridiance = []
isIngredance = False

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
for ing in ingridiance:
    for r in freshRanges:
        if( ing >= r[0] and ing <= r[1]):
            freshCount += 1
            break
        
print( freshCount )
            
