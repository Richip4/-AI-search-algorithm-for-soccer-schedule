from and_tree import Session, Slot


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
    eveningGameSlots = []
    eveningPracticeSlots = []

    inputFile = open("input.txt", "r")
    lines = inputFile.readlines()

    for i in range(0, len(lines)):

        if "game slots" in lines[i].lower():
            i = i + 1
            while lines[i] != "\n":
                lines[i] = lines[i].replace(" ", "")
                lines[i] = lines[i].replace("\n", "")
                lines[i] = lines[i].replace(",", " ", 1)
                lines[i] = lines[i].replace(" ", ",")
                lines[i] = lines[i].replace(":", "")
                splited = lines[i].split(",")
                gameSlots.append(Slot(splited[0], int(splited[1]), int(splited[2]), int(splited[3]), False))
                i = i + 1

        if "practice slots" in lines[i].lower():
            i = i + 1
            while lines[i] != "\n":
                lines[i] = lines[i].replace(" ", "")
                lines[i] = lines[i].replace("\n", "")
                lines[i] = lines[i].replace(",", " ", 1)
                lines[i] = lines[i].replace(" ", ",")
                lines[i] = lines[i].replace(":", "")
                splited = lines[i].split(",")
                practiceSlots.append(Slot(splited[0], int(splited[1]), int(splited[2]), int(splited[3]), True))
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

    # creates subarray of gameSlot and practiceSlot that are evening slots
    for i in range(len(gameSlots)):
        if gameSlots[i].time >= 1800:
            eveningGameSlots.append(gameSlots[i])

    for i in range(len(practiceSlots)):
        if practiceSlots[i].time >= 1800:
            eveningPracticeSlots.append(practiceSlots[i])

# uncomment following AND "parser()" to print parsing output
# gameSlots, practiceSlots, eveningGameSlots, and eveningPracticeSlots are Slot objects
# games and practices are Session objects
    # for i in range(len(gameSlots)):
    #     print("game slot", i, ":", gameSlots[i])
    # for i in range(len(practiceSlots)):
    #     print("prac slot", i, ":", practiceSlots[i])
    # for i in range(len(games)):
    #     print("game", i, ":", games[i])
    # for i in range(len(practices)):
    #     print("practice", i, ":", practices[i])
    # print("not compatible:", notCompatible)
    # print("unwanted:", unwanted)
    # print("preferences:", preferences)
    # print("pair:", pair)
    # print("partial assignments:", partialAssignments)
    # for i in range(len(eveningGameSlots)):
    #     print("evening game slot", i, ":", eveningGameSlots[i])
    # for i in range(len(eveningPracticeSlots)):
    #     print("evening prac slot", i, ":", eveningPracticeSlots[i])
    
    return gameSlots, practiceSlots, games, practices, notCompatible, unwanted, preferences, pair, partialAssignments, eveningGameSlots, eveningPracticeSlots

parser()