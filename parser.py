gameSlots = []
practiceSlots = []
games = []
practices = []
notCompatible = []
unwanted = []
preferences = []
pair = []
partialAssignments = []

inputFile = open("input.txt", "r")
lines = inputFile.readlines()

for i in range(0, len(lines)):

    if "game slots" in lines[i].lower():
        i = i + 1
        while lines[i] != "\n":
            gameSlots.append(lines[i].replace("\n", ""))
            i = i + 1

    if "practice slots" in lines[i].lower():
        i = i + 1
        while lines[i] != "\n":
            practiceSlots.append(lines[i].replace("\n", ""))
            i = i + 1

    if "games" in lines[i].lower():
        i = i + 1
        while lines[i] != "\n":
            games.append(lines[i].replace("\n", ""))
            i = i + 1

    if "practices" in lines[i].lower():
        i = i + 1
        while lines[i] != "\n":
            practices.append(lines[i].replace("\n", ""))
            i = i + 1

    if "not compatible" in lines[i].lower():
        i = i + 1
        while lines[i] != "\n":
            notCompatible.append(lines[i].replace("\n", ""))
            i = i + 1

    if "unwanted" in lines[i].lower():
        i = i + 1
        while lines[i] != "\n":
            unwanted.append(lines[i].replace("\n", ""))
            i = i + 1

    if "preferences" in lines[i].lower():
        i = i + 1
        while lines[i] != "\n":
            preferences.append(lines[i].replace("\n", ""))
            i = i + 1

    if "pair" in lines[i].lower():
        i = i + 1
        while lines[i] != "\n":
            pair.append(lines[i].replace("\n", ""))
            i = i + 1

    if "partial assignments" in lines[i].lower():
        i = i + 1
        while lines[i] != "\n":
            partialAssignments.append(lines[i].replace("\n", ""))
            i = i + 1
            if i == len(lines):
                break

inputFile.close()

print("games slot:", gameSlots)
print("practice slot:", practiceSlots)
print("games:", games)
print("practices:", practices)
print("not compatible:", notCompatible)
print("unwanted:", unwanted)
print("preferences:", preferences)
print("pair:", pair)
print("partial assignments:", partialAssignments)