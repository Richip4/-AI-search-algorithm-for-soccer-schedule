import parser as pS
import and_tree as aTree
import checks as check
import copy

#does fLeaf
def fLeaf(aRoot, aVisited, aLeafNodes):
    #find all the leaf nodes
    visited = aVisited
    leafNodes = aLeafNodes
    findLeafNodes(visited, leafNodes, aRoot)

#finds all the leaf nodes in the tree
def findLeafNodes(visited, leafNodes, node):
    if node not in visited:
        visited.add(node)
        if (len(node.children) == 0):
            leafNodes.add(node)
            return None
        else:
            for child in node.children:
                findLeafNodes(visited, leafNodes, child)

#generates all the divisions for a leaf and adds them to the tree
def div(aLeafNode, games, practices):
    #don't run div if a leaf is already solved
    if (aLeafNode.solved == True):
        return None

    gameSchedule = aLeafNode.game_schedule
    theGames = copy.copy(games)
    allGamesAssigned = False
    allPracticesAssigned = False
    isSolvable = False

    #check which games are not assigned yet
    for i in list(gameSchedule.keys()):
        if(len(gameSchedule[i]) > 0):
            for a in gameSchedule[i]:
                for b in theGames:
                    if(a.fullname == b.fullname):
                        theGames.remove(b)

    #generate all possible assignments of each game not assigned yet and add them as leafs
    for i in theGames:
        for key in list(gameSchedule.keys()):
            newSchedule = {}
            for a in list(gameSchedule.keys()):
                newSchedule[a] = list(gameSchedule[a])
            newSchedule[key].append(i)
            newNode = aTree.Node(newSchedule, aLeafNode.practice_schedule, aLeafNode, [])
            if(check.check_hard_constraints(newNode, input[4], input[5], input[9], input[10])):
                aLeafNode.children.append(newNode)
                isSolvable = True

    #check if all the games are assigned
    if len(theGames) == 0:
        allGamesAssigned = True
    #check if leaf can't be expanded with games without violating the hard constraints 
    if (allGamesAssigned == False and isSolvable == False):
        aLeafNode.solved = True

    isSolvable = False
    practiceSchedule = aLeafNode.practice_schedule
    thePractice = copy.copy(practices)

    #check which practices are not assigned yet 
    for i in list(practiceSchedule.keys()):
        if(len(practiceSchedule[i]) > 0):
            for a in practiceSchedule[i]:
                for b in thePractice:
                    if(a.fullname.replace(" ", "") == b.fullname.replace(" ", "")):
                        thePractice.remove(b)

    #check if all practices are assigned
    if len(thePractice) == 0:
        allPracticesAssigned = True

    #generate all possible assignments of each practice not assigned yet and add them as leafs
    for i in thePractice:
        for key in list(practiceSchedule.keys()):
            newSchedule = {}
            for a in list(practiceSchedule.keys()):
                newSchedule[a] = list(practiceSchedule[a])
            newSchedule[key].append(i)
            newNode = aTree.Node(aLeafNode.game_schedule, newSchedule, aLeafNode, [])
            if(check.check_hard_constraints(newNode, input[4], input[5], input[9], input[10])):
                aLeafNode.children.append(newNode)
                isSolvable = True

    #check if all games and practices assigned 
    if(allGamesAssigned and allPracticesAssigned):
        aLeafNode.solved = True
    #check if leaf can't be expanded with practices without violating the hard constraints 
    if (allPracticesAssigned == False and isSolvable == False):
        aLeafNode.solved = True

#function for assigning the evening slots
def doEveningSlots(aNode, eveningGameSlots, eveningPracticeSlots, games, practices):
    #assign games to evening slots
    for i in games:
        if (i.division >= 9):
            for a in eveningGameSlots:
                newSchedule = {}
                for b in list(gameSchedule.keys()):
                    newSchedule[b] = list(gameSchedule[b])
                newSchedule[a].append(i)
                newNode = aTree.Node(newSchedule, aNode.practice_schedule, aNode, [])
                aNode.children.append(newNode)

    #assigns practices to evening slots
    for i in practices:
        if (i.division >= 9):
            for a in eveningPracticeSlots:
                for a in eveningPracticeSlots:
                    newSchedule = {}
                    for b in list(practiceSchedule.keys()):
                        newSchedule[b] = list(practiceSchedule[b])
                newSchedule[a].append(i)
                newNode = aTree.Node(aNode.game_schedule, newSchedule, aNode, [])
                aNode.children.append(newNode)

#function for running the And-Tree Search
def a_tree(node, games, practices, notCompatible):
    notSolved = True

    while(notSolved):
        visited = set()
        leafNodes = set()
        fLeaf(node, visited, leafNodes)

        minEval = 1000000
        isAllSolved = True
        chosenSol = None
        
        #check if all leafs are solved
        for aLeafNode in leafNodes:
            if (aLeafNode.solved == False):
                isAllSolved = False

        #if all leafs solved find leaf with minimum eval 
        if(isAllSolved):
            notSolved = False
            for aLeafNode in leafNodes:
                leafNodeEval = check.check_soft_constraints(aLeafNode, input[6], input[15],input[17], input[7], input[16], input[14], input[11], input[13], input[12], input[14])
                if(check.is_complete_schedule(aLeafNode, games, practices) and leafNodeEval <= minEval):
                    minEval = leafNodeEval
                    chosenSol = aLeafNode
            
            return chosenSol

        #else run div on all leafs
        else:
            for aLeafNode in leafNodes:
                if (aLeafNode.solved == False):
                    div(aLeafNode, games, practices)

#get input from parser and declare problem data structure
input = pS.parser()
gameSchedule = {}
practiceSchedule = {}

#assign game slots in schedule
for i in input[0]:
    gameSchedule[i] = []

#assign practice slots in schedule
for i in input[1]:
    practiceSchedule[i] = []

doesSpecialExist = False
checkSpecial = False

#create special bookings 
for game in input[2]:
    if("CMSA U12T1" in game.fullname):
        checkSpecial = True
        for slot in list(practiceSchedule.keys()):
            if(slot.day == "TU" and slot.time == 1800):
                doesSpecialExist = True
                newSes = aTree.Session("CMSA U12T1S", 0, True, "CMSA U12T1S")
                practiceSchedule[slot].append(newSes)
    elif("CMSA U13T1" in game.fullname):
        checkSpecial = True
        for slot in list(practiceSchedule.keys()):
            if(slot.day == "TU" and slot.time == 1800):
                doesSpecialExist = True
                newSes = aTree.Session("CMSA U13T1S", 0, True, "CMSA U13T1S")
                practiceSchedule[slot].append(newSes)

if (checkSpecial == True and doesSpecialExist == False):
    print("Cannot create valid schedule from input. Needs to make special booking at TU 18:00 but that slot does not exist.")
    quit()

#do partial assignments
for partAssign in input[8]:
    if partAssign[0].is_practice:
        for slot in list(practiceSchedule.keys()):
            if (slot.day in partAssign[1] and slot.time == partAssign[2]):
                practiceSchedule[slot].append(partAssign[0])
                for b in input[3]:
                    if(partAssign[0].fullname == b.fullname):
                        input[3].remove(b)
    else:
        for slot in list(gameSchedule.keys()):
            if (slot.day in partAssign[1] and slot.time == partAssign[2]):
                gameSchedule[slot].append(partAssign[0])
                for b in input[2]:
                    if(partAssign[0].fullname == b.fullname):
                        input[2].remove(b)

#create root node
root = aTree.Node(gameSchedule, practiceSchedule, None, [])
andTree = aTree.Tree(root)

#assign evening slots
doEveningSlots(root, input[9], input[10], input[2], input[3])

#do And-Tree search and generate solution node
final = a_tree(root, input[2], input[3], input[4])

#check if solution is possible
if (final == None):
    print("Cannot create valid schedule from input.")
    quit()

#Printing output-----------------------

gameSchedule = final.game_schedule
practiceSchedule = final.practice_schedule

#generate eval value by checking soft constraints
evalVal = check.check_soft_constraints(final, input[6], input[15],input[17], input[7], input[16], input[18], input[11], input[13], input[12], input[14])

print("Eval-value:", evalVal)

#print games
for slot, sList in gameSchedule.items():
    if(slot.time >= 1000):
        time = str(slot.time)
        time = time[:2] + ":" + time[2:]
    else:
        time = str(slot.time)
        time = time[:1] + ":" + time[1:]
    for session in sList:
        print('{:<30s} {:<10s}'.format(session.fullname, ":" + slot.day + ", " + time))

#print practices
for slot, sList in practiceSchedule.items():
    if(slot.time >= 1000):
        time = str(slot.time)
        time = time[:2] + ":" + time[2:]
    else:
        time = str(slot.time)
        time = time[:1] + ":" + time[1:]
    for session in sList:
        print('{:<30s} {:<10s}'.format(session.fullname, ":" + slot.day + ", " + time))