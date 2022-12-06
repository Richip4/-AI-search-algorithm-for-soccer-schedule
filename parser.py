from and_tree import Session


def parser():
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
                lines[i] = lines[i].replace(" ", "")
                lines[i] = lines[i].replace("\n", "")
                lines[i] = lines[i].replace(",", " ", 1)
                splited = lines[i].split(",")
                gameSlots.append(splited)
                i = i + 1

        if "practice slots" in lines[i].lower():
            i = i + 1
            while lines[i] != "\n":
                lines[i] = lines[i].replace(" ", "")
                lines[i] = lines[i].replace("\n", "")
                lines[i] = lines[i].replace(",", " ", 1)
                splited = lines[i].split(",")
                practiceSlots.append(splited)
                i = i + 1

        if "games" in lines[i].lower():
            i = i + 1
            while lines[i] != "\n":
                lines[i] = lines[i].replace("\n", "")
                splited = lines[i].split(" ")
                print(splited[0] + " " + splited[1])
                games.append(Session(splited[0] + " " + splited[1], int(splited[3]), False))
                i = i + 1

        if "practices" in lines[i].lower():
            i = i + 1
            while lines[i] != "\n":
                lines[i] = lines[i].replace("\n", "")
                splited = lines[i].split(" ")
                print(splited[0] + " " + splited[1])
                practices.append(Session(splited[0] + " " + splited[1], int(splited[3]), True))
                i = i + 1

        if "not compatible" in lines[i].lower():
            i = i + 1
            while lines[i] != "\n":
                lines[i] = lines[i].replace("\n", "")
                splited = lines[i].split(", ")
                notCompatible.append(splited)
                i = i + 1

        if "unwanted" in lines[i].lower():
            i = i + 1
            while lines[i] != "\n":
                lines[i] = lines[i].replace("\n", "")
                splited = lines[i].split(", ", 1)
                splited[1] = splited[1].replace(", ", " ")
                unwanted.append(splited)
                i = i + 1

        if "preferences" in lines[i].lower():
            i = i + 1
            while lines[i] != "\n":
                lines[i] = lines[i].replace("\n", "")
                lines[i] = lines[i].replace(", ", " ", 1)
                splited = lines[i].split(", ")
                preferences.append(splited)
                i = i + 1

        if "pair" in lines[i].lower():
            i = i + 1
            while lines[i] != "\n":
                lines[i] = lines[i].replace("\n", "")
                splited = lines[i].split(", ")
                pair.append(splited)
                i = i + 1

        if "partial assignments" in lines[i].lower():
            # i = i + 1
            while lines[i] != "\n":
                i = i + 1
                if i == len(lines):
                    break
                lines[i] = lines[i].replace("\n", "")
                splited = lines[i].split(", ", 1)
                splited[1] = splited[1].replace(", ", " ")
                partialAssignments.append(splited)
                # i = i + 1
                # if i == len(lines):
                #    break

    inputFile.close()

    
    print("games slot:", gameSlots)
    print("practice slot:", practiceSlots)
    
    for i in range(len(games)):
        print("game", i, ":", games[i])
    for i in range(len(practices)):
        print("practice", i, ":", practices[i])
    print("not compatible:", notCompatible)
    print("unwanted:", unwanted)
    print("preferences:", preferences)
    print("pair:", pair)
    
    print("partial assignments:", partialAssignments)
    return gameSlots, practiceSlots, games, practices, notCompatible, unwanted, preferences, pair, partialAssignments

parser()