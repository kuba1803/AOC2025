lineToProccess = ""


with open('data.txt') as f:
    for line in f:
        lineToProccess += line.strip()


ranges = lineToProccess.split(",")
result = 0

for rangeRow in ranges:
    rangeLimit: list[str] = rangeRow.split("-")
    if len(rangeLimit[0])%2==1:
        rangeLimit[0]=str(10**len(rangeLimit[0]))
    if len(rangeLimit[1]) % 2 == 1:
        rangeLimit[1] = str((10 ** (len(rangeLimit[1])-1))-1)
    lowerLimit = int(rangeLimit[0])
    upperLimit = int(rangeLimit[1])
    lower = int(rangeLimit[0][:int(len(rangeLimit[0])/2)])
    upper = int(rangeLimit[1][:int(len(rangeLimit[1])/2)])+1
    for i in range(lower,upper):
        testString = str(i) + str(i);
        testNumber = int(testString)
        if testNumber >= lowerLimit and  testNumber <= upperLimit:
            result += testNumber
    print(rangeLimit)
print(result)