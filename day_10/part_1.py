result = 0

with open('data.txt') as f:
    for line in f:
        l = line.strip().split()
        light = 0
        for idx in range(1,len(l[0])-1):
            if(l[0][idx]=='#'):
               light|=1<<(idx-1)

        buttons = []
        for idx in range(1,len(l)-1):
            button = 0
            wire = list(map(int, l[idx][1:-1].strip().split(",")))
            for w in wire:
                button |= 1<<w
            buttons.append(button)

        lightDist = dict([(light,0)])
        stack =[light]
        while len(stack)>0:
            key = stack.pop()
            totalCost = lightDist[key]
            for button in buttons:
                newKey = key ^ button
                newCost = totalCost + 1
                if newKey not in lightDist:
                    lightDist[newKey]=newCost
                    stack.append(newKey)
                    continue

                if newCost < lightDist[newKey]:
                    lightDist[newKey]=newCost
                    stack.append(newKey)
                    continue

        result += lightDist[0]

print(result)












