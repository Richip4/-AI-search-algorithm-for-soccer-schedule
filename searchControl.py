#for Fleaf, Ftrans and DIV
import and_tree as aTree
import checks as check
import random


#Will choose which leaf to try and expand (current idea is to randomly choose leaf)
def fLeaf(aTree):
    #find all the leaf nodes
    visited = set()
    leafNodes = set()
    findLeafNodes(visited, leafNodes, aTree.root)
    
    #randomly generate a number within the bounds of the leaf node list and choose that leaf node
    childrenSize = len(leafNodes)
    leafIndex = random.randint(0,childrenSize-1)
    chosenLeaf = leafNodes[leafIndex]

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
                theGames.remove(a)
             
    for i in theGames:
        for key in list(gameSchedule.keys()):
            newSchedule = gameSchedule.copy()
            newSchedule[key].append(i)
            newNode = aTree.Node(newSchedule, aLeafNode.practices, aLeafNode,               [])
            if(check.check_hard_constraints(newNode, check.notCompatible, check.unwanted)):
                aLeafNode.children.append(newNode)

    practiceSchedule = aLeafNode.practice_schedule.copy()
    thePractice = check.practice.copy()
    for i in list(practiceSchedule.keys()):
        if(practiceSchedule[i]):
            for a in practiceSchedule[i]:
                check.thePractices.remove(a)
                
        for i in thePractice:
            for key in list(check.PracticeSchedule.keys()):
                newSchedule = practiceSchedule.copy()
                newSchedule[key].append(i)
                newNode = aTree.Node(gameSchedule, practiceSchedule, aLeafNode,               [])
                if(check.check_hard_constraints(newNode, check.notCompatible, check.unwanted)):
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

'''
games slot: [['MO 8:00', '3', '2'], ['MO 9:00', '3', '2'], ['TU 9:30', '2', '1']]
practice slot: [['MO 8:00', '4', '2'], ['TU 10:00', '2', '1'], ['FR 10:00', '2', '1']]
partial assignments: [['CUSA O18 DIV 01', 'MO 8:00'], ['CUSA O18 DIV 01 PRC 01', 'FR 10:00']]
'''
# gameSlots =[['MO 8:00', '3', '2'], ['MO 9:00', '3', '2'], ['TU 9:30', '2', '1']]
# practiceSlots = [['MO 8:00', '4', '2'], ['TU 10:00', '2', '1'], ['FR 10:00', '2', '1']]

# root = aTree.Node(gameSlots, practiceSlots, None)
# andTree = aTree.Tree(root)
# node1 = aTree.Node(None, None, None)
# node2 = aTree.Node(gameSlots, practiceSlots[1:1], node1)
# root.children.append(node1)
# node1.children.append(node2)
# node3 = aTree.Node(None, None, None)
# node1.children.append(node3)

# newNode = aTree.Node(None, None, None)


# leafNodes = set()
# visited = set()

# print(findLeafNodes(visited, leafNodes, root))
# print(node3)
# print(node2)
# print(leafNodes)
# slot = aTree.Slot("MON", 1900, 3, 1, False)
# slot2 = aTree.Slot("TUE", 200, 3, 1, False)
# ses1 = aTree.Session("jkl", 9, True)
# ses2 = aTree.Session("lkm", 10, True)
# ps = {slot: [], slot2: []}
# #games = [ses1, ses2]
# leafNode = aTree.Node(None, ps, None, [])

# evGs = []
# evPs = [slot]
# games = []
# practices = [ses1, ses2]
# doEveningSlots(leafNode, evGs, evPs, games, practices)
# print(ses1.division)
# print(leafNode.children)
