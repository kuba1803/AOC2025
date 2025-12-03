lineToProccess = ""

def find_first_max_id( str, beginIdx, endIdx ):
    maxIdx = beginIdx;
    max = int(str[maxIdx:maxIdx+1])
    for idx in range(maxIdx+1,endIdx):
        digit = int(str[idx:idx+1])
        if( digit > max ):
            maxIdx = idx
            max = digit
    print( f'maxIdx {maxIdx} = digit {max}' )
    return maxIdx

def get_number( str, digitNumber ):
    startIdx = 0
    result = 0
    print( str )
    for i in range( digitNumber-1, -1, -1 ):
        maxIdx = find_first_max_id( str, startIdx, len( str ) - i )
        result = result * 10 + int(str[maxIdx:maxIdx+1])
        startIdx = maxIdx + 1
    print( result )
    return result

result = 0

with open('data.txt') as f:
    for line in f:
        lineToProccess = line.strip()
        result += get_number( lineToProccess, 12 )
        print( lineToProccess )

print(result)