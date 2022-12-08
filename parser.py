from and_tree import Session, Slot
import sys

def parser():

    fileName = sys.argv[1]
    wminfilled = sys.argv[2]
    wpref = sys.argv[3]
    wpair = sys.argv[4]
    wsecdiff = sys.argv[5]
    penGameMin = sys.argv[6]
    penPracticeMin = sys.argv[7]
    penNotPaired = sys.argv[8]
    penSection = sys.argv[9]

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

    inputFile = open(fileName, "r")
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
                fullname = lines[i]
                splited = lines[i].split(" ")
                games.append(Session(splited[0] + " " + splited[1], int(splited[3]), False, fullname))
                i = i + 1

        if "practices" in lines[i].lower():
            i = i + 1
            while lines[i] != "\n":
                lines[i] = lines[i].replace("\n", "")
                fullname = lines[i]
                splited = lines[i].split(" ")
                practices.append(Session(splited[0] + " " + splited[1], int(splited[3]), True, fullname))
                i = i + 1

        if "not compatible" in lines[i].lower():
            i = i + 1
            while lines[i] != "\n":
                lines[i] = lines[i].replace("\n", "")
                splited = lines[i].split(", ")
                if splited[1][-1] == " ":
                    splited[1] = splited[1][:-1]
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
                name = splited[0]
                if len(splited) > 1:
                    splited[1] = splited[1].split(", ")
                    splited[0] = splited[0].split(" ")
                    splited[1][1] = int(splited[1][1].replace(":", ""))
                    if "PRC" in splited[0]:
                        partialAssignments.append([Session(splited[0][0] + splited[0][1], int(splited[0][3]), True, name), splited[1][0], splited[1][1]])
                    else:
                        partialAssignments.append([Session(splited[0][0] + splited[0][1], int(splited[0][3]), False, name), splited[1][0], splited[1][1]])
                # i = i + 1
                # if i == len(lines):
                #    break

    inputFile.close()

    gameAndPracNames = []
    for i in range(len(games)):
        gameAndPracNames.append(games[i].fullname)
    for i in range(len(practices)):
        gameAndPracNames.append(practices[i].fullname)

    for i in range(len(preferences)):
        if (preferences[i][1] in gameAndPracNames) == False:
            print("Session " + preferences[i][1] + " in preferences is not a game or practice")    
            quit()

    for i in range(len(unwanted)):
            if (unwanted[i][0] in gameAndPracNames) == False:
                print("Session " + unwanted[i][0] + " in unwanted is not a game or practice")    
                quit()

    for i in range(len(partialAssignments)):
            if (partialAssignments[i][0].fullname in gameAndPracNames) == False:
                print("Session " + partialAssignments[i][0].fullname + " in partial assignments is not a game or practice")    
                quit()
            # if (partialAssignments[i][0].is_practice == False):
            #     slotExists = False
            #     for j in range(len(gameSlots)):
            #         if gameSlots[i].day == partialAssignments[i][1] and gameSlots[i].time == partialAssignments[i][2]:
            #             slotExists = True
            #             break
            # elif (partialAssignments[i][0].is_practice == True):
            #                 slotExists = False
            #                 for j in range(len(practiceSlots)):
            #                     if practiceSlots[i].day == partialAssignments[i][1] and practiceSlots[i].time == partialAssignments[i][2]:
            #                         slotExists = True
            #                         break
            # if slotExists == False:
            #     print("Slot " + partialAssignments[i][1] + str(partialAssignments[i][2]) + " for " + partialAssignments[i][0].fullname + " does not exist")
            #     quit()

    for i in range(len(pair)):
        if (pair[i][0] in gameAndPracNames) == False:
            print("Session " + pair[i][0] + " in pairs is not a game or practice")  
            quit()  
        elif (pair[i][1] in gameAndPracNames) == False:
            print("Session " + pair[i][1] + " in pairs is not a game or practice") 
            quit()

    for i in range(len(notCompatible)):
        if (notCompatible[i][0] in gameAndPracNames) == False:
            print("Session " + notCompatible[i][0] + " in notCompatible is not a game or practice")  
            quit()  
        elif (notCompatible[i][1] in gameAndPracNames) == False:
            print("Session " + notCompatible[i][1] + " in notCompatible is not a game or practice") 
            quit()

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
    # for i in range(len(prefTemp)):
    #     print("pref", i, ":", prefTemp[i])
    # print("pair:", pair)
    # print("partial assignments:", partialAssignments)
    # for i in range(len(eveningGameSlots)):
    #     print("evening game slot", i, ":", eveningGameSlots[i])
    # for i in range(len(eveningPracticeSlots)):
    #     print("evening prac slot", i, ":", eveningPracticeSlots[i])

    return [gameSlots, practiceSlots, games, practices, notCompatible, unwanted, preferences, pair, partialAssignments, eveningGameSlots, eveningPracticeSlots, int(wminfilled), int(wpair), int(wpref), int(wsecdiff), int(penGameMin), int(penNotPaired), int(penPracticeMin), int(penSection)]

parser()