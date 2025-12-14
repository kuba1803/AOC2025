result = 0

systems = "systems = {"

with open('example.txt') as f:
    for line in f:
        print(line)
        l = line.strip().split()

        joltages = list(map(int, l[len(l)-1][1:-1].strip().split(",")))
        print(len(joltages))
        system = "{"
        equasion = [""]*len(joltages)

        for idx in range(1,len(l)-1):
            wire = list(map(int, l[idx][1:-1].strip().split(",")))
            print(wire)
            for w in wire:
                equasion[w] = equasion[w] + "x" + str(idx-1) + " + "

        for s in range(len(equasion)):
            equasion[s] = equasion[s][:-2] + " == " + str(joltages[s])
            system += equasion[s] + ","
        system = system[:-1] + "},"
        print(system)
        systems += system


systems = systems[:-1] + "};"

print(systems)












