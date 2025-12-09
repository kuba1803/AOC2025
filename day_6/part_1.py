rows = []
operators = []

with open('data.txt') as f:
    for line in f:
        row = line.strip().split()
        if( row[0].isdigit() ):
            rows.append( list(map(int,row)))
        else:
            operators = row

result = 0

for opIdx in range(len(operators)):
    if( operators[opIdx] == "+" ):
        subResult = 0
        for rowIdx in range(len(rows)):
            subResult += rows[rowIdx][opIdx]
        result += subResult
    elif (operators[opIdx] == "*"):
        subResult = 1
        for rowIdx in range(len(rows)):
            subResult *= rows[rowIdx][opIdx]
        result += subResult

print( result )
        

            
