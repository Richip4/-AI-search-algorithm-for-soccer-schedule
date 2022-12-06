import parser as pS
import and_tree as aT
import checks as checks
import searchControl as sC

def a_tree(node, games, practices):
    notSolved = False

    while(notSolved == False):
        chosenLeaf = sC.fLeaf(node)
        sC.div(chosenLeaf, games, practices)
        #check solved
    
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

    score = checks.check_soft_constraints(node)
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
    if partAssign[0].isPractice:
        practiceSchedule[partAssign[1]].append(partAssign[0])
    else:
        gameSchedule[partAssign[1]].append(partAssign[0])

# print(initial_game_input)
# print(initial_practice_input)

# and_tree = Tree(Node(initial_game_input, initial_practice_input, None))

# a_tree(and_tree.root)

root = aT.Node(gameSchedule, practiceSchedule, None, [])
andTree = aT.Tree(root)

sC.doEveningSlots(root, input[9], input[10], input[2], input[3])

#Printing output-----------------------

# aGame = Slot('MO', '8:00', 2, 0, False)
# aGSession = Session("CSMA U13T3", 99, False, "CSMA U13T3 DIV 99")

# aPractice = Slot('MO', '8:00', 2, 0, True)
# aPSession1 = Session('CSMA U13T3', 1, True, "CSMA U13T3 DIV 99 OPN 01")
# aPSession2 = Session('CSSC O19T1', 1, True, "CSSC O19T1 DIV 01 PRC 01")

# game_sch = {aGame:[aGSession]}  # Placeholder
# prac_sch = {aPractice:[aPSession1, aPSession2]}  # Placeholder
#game_sch = {aGame:['CSMA U13T3 DIV 01'], 'MO, 9:00':['CSMA U17T1 DIV 01'], 'TO, 9:30':[]}
#prac_sch = {'MO, 8:00':['CSMA U13T3 DIV 02 OPN 02','CSMA U17T1 PRC 01'], 'TU, 10:00':['CSSC O19T1 DIV 95 PRC 99'], 'FR, 10:00':['CUSA O18 DIV 01 PRC 01']}

#game_sch and prac_sch as 'placeholders' for game_schedule and practice_schedule dictionaries
print("Eval-value: ")
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
    for session in sList:
        print('{:<30s} {:<10s}'.format(session.fullname, ":" + slot.day + ", " + time))


