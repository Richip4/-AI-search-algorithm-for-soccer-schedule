import parser as pS
import and_tree as aTree
import checks as check
import random
import copy
#import searchControl as sC

def fLeaf(aRoot, aVisited, aLeafNodes):
    #find all the leaf nodes
    visited = aVisited
    leafNodes = aLeafNodes
    allSolved = True
    findLeafNodes(visited, leafNodes, aRoot)
    
    #randomly generate a number within the bounds of the leaf node list and choose that leaf node
    childrenSize = len(leafNodes)

    leafIndex = random.randint(0,childrenSize-1)
    chosenLeaf = list(leafNodes)[leafIndex]
    #chosenLeaf = leafNodes[leafIndex]

    #return chosenLeaf 

def findLeafNodes(visited, leafNodes, node):
    if node not in visited:
        visited.add(node)
        if (len(node.children) == 0):
            leafNodes.add(node)
            return None
        else:
            for child in node.children:
                findLeafNodes(visited, leafNodes, child)


def div(aLeafNode, games, practices):
    #print("Running DIV")
    # if (check.is_complete_schedule(aLeafNode, input[2], input[3])):
    #     aLeafNode.solved = True

    if (aLeafNode.solved == True):
        return None

    gameSchedule = aLeafNode.game_schedule
    theGames = copy.copy(games)
    allGamesAssigned = False
    allPracticesAssigned = False
    isSolvable = False

    for i in list(gameSchedule.keys()):
        if(len(gameSchedule[i]) > 0):
            for a in gameSchedule[i]:
                for b in theGames:
                    if(a.fullname == b.fullname):
                        theGames.remove(b)

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

    if len(theGames) == 0:
        allGamesAssigned = True
    if (allGamesAssigned == False and isSolvable == False):
        aLeafNode.solved = True

    isSolvable = False
    practiceSchedule = aLeafNode.practice_schedule
    thePractice = copy.copy(practices)

    for i in list(practiceSchedule.keys()):
        if(len(practiceSchedule[i]) > 0):
            for a in practiceSchedule[i]:
                for b in thePractice:
                    if(a.fullname.replace(" ", "") == b.fullname.replace(" ", "")):
                        thePractice.remove(b)

    if len(thePractice) == 0:
        allPracticesAssigned = True

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
            
    if(allGamesAssigned and allPracticesAssigned):
        aLeafNode.solved = True
    if (allPracticesAssigned == False and isSolvable == False):
        aLeafNode.solved = True
    if(isSolvable == False):
        aLeafNode.solved == True

def doEveningSlots(aNode, eveningGameSlots, eveningPracticeSlots, games, practices):
    for i in games:
        if (i.division >= 9):
            for a in eveningGameSlots:
                newSchedule = {}
                for b in list(gameSchedule.keys()):
                    newSchedule[b] = list(gameSchedule[b])
                newSchedule[a].append(i)
                newNode = aTree.Node(newSchedule, aNode.practice_schedule, aNode, [])
                aNode.children.append(newNode)

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


def a_tree(node, games, practices, notCompatible):
    notSolved = True
    i = 0
    while(notSolved):
        visited = set()
        leafNodes = set()
        #chosenLeaf = fLeaf(node, visited, leafNodes)
        fLeaf(node, visited, leafNodes)
        minEval = 1000
        isAllSolved = True
        chosenSol = None
        #print(chosenLeaf)
        # if (check.is_complete_schedule(chosenLeaf, games ,practices)):
        #     notSolved = False 
        #     return chosenLeaf
        for aLeafNode in leafNodes:
            if (aLeafNode.solved == False):
                isAllSolved = False

        if(isAllSolved):
            notSolved = False
            for aLeafNode in leafNodes:
                leafNodeEval = check.check_soft_constraints(aLeafNode, input[6], input[15],input[17], input[7], input[16], input[14], input[11], input[13], input[12], input[14])
                if(check.is_complete_schedule(aLeafNode, games, practices) and leafNodeEval <= minEval):
                    minEval = leafNodeEval
                    chosenSol = aLeafNode
            
            return chosenSol

        else:
            for aLeafNode in leafNodes:
                if (aLeafNode.solved == False):
                    div(aLeafNode, games, practices)

best_score = 9999999
def check_save(node):
    for slot in node.game_schedule:
        if len(node.game_schedule[slot]) < game_min_dict[slot]:
            return False

    for slot in node.practice_schedule:
        if len(node.practice_schedule[slot]) < practice_min_dict[slot]:
            return False

    score = check.check_soft_constraints(node)
    global best_score
    if score < best_score:
        global best_node
        best_node = node
        best_score= score

#gameSlots, practiceSlots, games, practices, notCompatible, unwanted, preferences, pair, partialAssignments = parser()
input = pS.parser()
gameSchedule = {}
practiceSchedule = {}
for i in input[0]:
    gameSchedule[i] = []

for i in input[1]:
    practiceSchedule[i] = []

# change gameslots variable into a dict
# game_max_dict = {}
# game_min_dict = {}
# for slot in gameSlots:
#     game_max_dict[slot[0]] = slot[1]
#     game_min_dict[slot[0]] = slot[2]

# # change practiceslots variable into a dict
# practice_max_dict = {}
# practice_min_dict = {}
# for slot in practiceSlots:
#     practice_max_dict[slot[0]] = slot[1]
#     practice_min_dict[slot[0]] = slot[2]

# initial_game_input = {}
# initial_practice_input = {}

# for part_assign in input[8]:
#     if checks.is_practice(part_assign[0]):
#         if part_assign[1] in initial_practice_input:
#             initial_practice_input[part_assign[1]].append(part_assign[0])
#         else:
#             initial_practice_input[part_assign[1]] = [ part_assign[0] ]
#     else:
#         if part_assign[1] in initial_game_input:
#             initial_game_input[part_assign[1]].append(part_assign[0])
#         else:
#             initial_game_input[part_assign[1]] = [ part_assign[0] ]

doesSpecialExist = False
checkSpecial = False

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

for partAssign in input[8]:
    if partAssign[0].is_practice:
        for slot in list(practiceSchedule.keys()):
            if (slot.day in partAssign[1] and slot.time == partAssign[2]):
                #print("slot day: ", slot.day, "slot time ", slot.time, " practice.time ", partAssign[2])
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

# print(initial_game_input)
# print(initial_practice_input)

# and_tree = Tree(Node(initial_game_input, initial_practice_input, None))

# a_tree(and_tree.root)

#print(gameSchedule)
root = aTree.Node(gameSchedule, practiceSchedule, None, [])
andTree = aTree.Tree(root)

doEveningSlots(root, input[9], input[10], input[2], input[3])

final = a_tree(root, input[2], input[3], input[4])

if (final == None):
    print("Cannot create valid schedule from input.")
    quit()

#print(gameSchedule)
#print(root.children)


#Printing output-----------------------

gameSchedule = final.game_schedule
practiceSchedule = final.practice_schedule
#print("FINAL")
evalVal = check.check_soft_constraints(final, input[6], input[15],input[17], input[7], input[16], input[18], input[11], input[13], input[12], input[14])
#print(practiceSchedule)
#print(gameSchedule[input[0][0]])
#print(gameSchedule[input[0][1]])
print("Eval-value:", evalVal)
for slot, sList in gameSchedule.items():
    if(slot.time >= 1000):
        time = str(slot.time)
        time = time[:2] + ":" + time[2:]
    else:
        time = str(slot.time)
        time = time[:1] + ":" + time[1:]
    for session in sList:
        print('{:<30s} {:<10s}'.format(session.fullname, ":" + slot.day + ", " + time))

for slot, sList in practiceSchedule.items():
    if(slot.time >= 1000):
        time = str(slot.time)
        time = time[:2] + ":" + time[2:]
    else:
        time = str(slot.time)
        time = time[:1] + ":" + time[1:]
    for session in sList:
        print('{:<30s} {:<10s}'.format(session.fullname, ":" + slot.day + ", " + time))
