import parser as pS
import and_tree as aTree
import checks as check
import random
#import searchControl as sC

def fLeaf(aRoot):
    #find all the leaf nodes
    visited = set()
    leafNodes = set()
    findLeafNodes(visited, leafNodes, aRoot)
    
    #randomly generate a number within the bounds of the leaf node list and choose that leaf node
    childrenSize = len(leafNodes)
    leafIndex = random.randint(0,childrenSize-1)
    chosenLeaf = list(leafNodes)[leafIndex]

    return chosenLeaf 

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
    gameSchedule = aLeafNode.game_schedule.copy()
    theGames = games.copy()
    for i in list(gameSchedule.keys()):
        if(gameSchedule[i]):
            for a in gameSchedule[i]:
                # print("games list ", games)
                # print("theGames list ", theGames)
                # print("Game ", a)
                for b in theGames:
                    if(a.fullname == b.fullname):
                        theGames.remove(b)
             
    for i in theGames:
        for key in list(gameSchedule.keys()):
            newSchedule = gameSchedule.copy()
            newSchedule[key].append(i)
            newNode = aTree.Node(newSchedule, aLeafNode.practice_schedule, aLeafNode, [])
            if(check.check_hard_constraints(newNode, input[4], input[5], input[9], input[10])):
                aLeafNode.children.append(newNode)

    practiceSchedule = aLeafNode.practice_schedule.copy()
    thePractice = practices.copy()
    for i in list(practiceSchedule.keys()):
        if(practiceSchedule[i]):
            for a in practiceSchedule[i]:
                for b in thePractice:
                    if(a.fullname == b.fullname):
                        thePractice.remove(b)
                
        for i in thePractice:
            for key in list(practiceSchedule.keys()):
                newSchedule = practiceSchedule.copy()
                newSchedule[key].append(i)
                newNode = aTree.Node(gameSchedule, practiceSchedule, aLeafNode, [])
                if(check.check_hard_constraints(newNode, input[4], input[5], input[9], input[10])):
                    aLeafNode.children.append(newNode)


def doEveningSlots(aNode, eveningGameSlots, eveningPracticeSlots, games, practices):
    sizeOfEveGame = len(eveningGameSlots)
    sizeOfEvePract = len(eveningPracticeSlots)
    for i in games:
        if (i.division >= 9):
            for a in eveningGameSlots:
                newSchedule = aNode.game_schedule.copy()
                newSchedule[a].append(i)
                newNode = aTree.Node(aNode.game_schedule, aNode.practiceSchedule, aNode, [])
                aNode.children.append(newNode)

    for i in practices:
        if (i.division >= 9):
            for a in eveningPracticeSlots:
                print("adding practice", i.division)
                newSchedule = aNode.practice_schedule.copy()
                newSchedule[a].append(i)
                newNode = aTree.Node(aNode.game_schedule, newSchedule, aNode, [])
                aNode.children.append(newNode)


def a_tree(node, games, practices, notCompatible):
    notSolved = True

    while(notSolved):
        chosenLeaf = fLeaf(node)
        if (check.is_complete_schedule(chosenLeaf, games ,practices)):
            notSolved = False 
            return chosenLeaf

        else:
            div(chosenLeaf, games, practices)
    # # if all children are solved then solve yourself & move up
    # if not checks.check_hard_constraints(node, notCompatible):
    #     node.solved = True
    #     node = node.parent
    # elif checks.is_complete_schedule(node):
    #     check_save(node)
    #     node.solved = True
    #     node = node.parent
    # else:
    #     #div(node)
    #     for child in node.children:
    #         if not child.solved:
    #             a_tree(node)



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

for partAssign in input[8]:
    if partAssign[0].is_practice:
        for slot in list(practiceSchedule.keys()):
            if (slot.day in partAssign[1] and slot.time == partAssign[2]):
                print("slot day: ", slot.day, "slot time ", slot.time, " practice.time ", partAssign[2])
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

root = aTree.Node(gameSchedule, practiceSchedule, None, [])
andTree = aTree.Tree(root)

doEveningSlots(root, input[9], input[10], input[2], input[3])

final = a_tree(root, input[2], input[3], input[4])

#Printing output-----------------------

gameSchedule = final.game_schedule
practiceSchedule = final.practice_schedule
print("Eval-value: ", best_score)
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
