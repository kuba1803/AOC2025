rows = []
operators = []

with open('data.txt') as f:
    for line in f:
        if( line[0] == "*" or line[0]=="+"):
            operators = line
        else:
            rows.append( line.replace("\n", " ") )

numberRange = []
for opIdx in range(len(operators)):
    if( operators[opIdx] == "*" or operators[opIdx] == "+"):
        numberRange.append(opIdx)
operators = operators.split()
numberRange.append(999999)


for row in rows:
    print(str(row))
print(operators)
print(numberRange)

result = 0

for nrIdx in range(len(numberRange)-1):
    begin = numberRange[nrIdx]
    end = numberRange[nrIdx+1]
    numbers = []
    maxLen = 0
    for row in rows:
        num = ""
        if( end == 999999):
            num = str(row)[begin:len(row)]
            numbers.append(num)
        else:
            num = str(row)[begin:end]
            numbers.append(num)
        if (maxLen < len(num)):
            maxLen = len(num)

    subResult = 0
    print(operators[nrIdx])
    print(numbers)
    if( operators[nrIdx] == "*"):
        subResult+=1

    for idx in range(maxLen-1):
        numHor = ""
        for num in numbers:
            #print(num)
            if( idx < len(num) and num[idx]!=" " ):
                numHor = numHor + num[idx]
        if( len(numHor) == 0 ):
            continue
        #print(numHor)
        if( operators[nrIdx]=="*"):
            subResult *= int(numHor)
        else:
            subResult += int(numHor)
    print(f'sub {subResult}')
    result += subResult




print( result )

