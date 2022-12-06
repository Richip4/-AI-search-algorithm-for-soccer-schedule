#for Fleaf, Ftrans and DIV
import and_tree as aTree
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

#Will choose best transition for a leaf from div
#If can solve selected leaf, then solve. Else,
#Assign all part assignments
#Assign evening slots to >=DIV9
#Do all other possible combinations of assignments for each game and practice  
def fTrans(aLeaf):
    chosenTransition = None

    return chosenTransition

def doPartAssigns(aRoot, partAssigns):
    newNode = aTree.node()
    for i in partAssigns:
        aRoot.game_schedule.append(i)

def doEveningSlots(aNode, eveningGameSlots, eveningPracticeSlots, games, practices):
    sizeOfEveGame = len(eveningGameSlots)
    sizeOfEvePract = len(eveningPracticeSlots)
    for i in games:
        if (i.division >= 9):
            for a in eveningGameSlots:
                newPr = aTree.Node(aNode.game_schedule, aNode.practiceSchedule, aNode, [])
                newPr.game_schedule[a].append(i)

def findLeafNodes(visited, leafNodes, node):
    if node not in visited:
        visited.add(node)
        if (len(node.children) == 0):
            leafNodes.add(node)
            return None
        else:
            for child in node.children:
                findLeafNodes(visited, leafNodes, child)


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