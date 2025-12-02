lineToProccess = ""


with open('data.txt') as f:
    for line in f:
        lineToProccess += line.strip()


ranges = lineToProccess.split(",")
result = 0

for rangeRow in ranges:
    partSum = 0
    rangeLimit: list[str] = rangeRow.split("-")
    minPaternSize = 1
    maxPaternSize = int(len(rangeLimit[1])/2)
    for number in range(max(int(rangeLimit[0]),10),int(rangeLimit[1])+1):
        stringNumber = str(number)
        for size in range(minPaternSize, maxPaternSize + 1):
            if len(stringNumber)%size != 0:
                continue
            expectedCount = int(len(stringNumber)/size)
            if stringNumber.count(stringNumber[:size])==expectedCount:
                #print( f'parern {stringNumber[:size]} number {number}')
                result += number
                partSum += number
                break

    print(f'range {rangeLimit} part sum {partSum}')

print( f'result {result}')
