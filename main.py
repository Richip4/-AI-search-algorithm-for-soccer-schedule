from parser import parser
from and_tree import *
import checks as checks

def a_tree(node):
    # if all children are solved then solve yourself & move up
    if not checks.check_hard_constraints(node, notCompatible):
        node.solved = True
        node = node.parent
    elif checks.is_complete_schedule(node):
        check_save(node)
        node.solved = True
        node = node.parent
    else:
        #div(node)
        for child in node.children:
            if not child.solved:
                a_tree(node)


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

gameSlots, practiceSlots, games, practices, notCompatible, unwanted, preferences, pair, partialAssignments = parser()

# change gameslots variable into a dict
game_max_dict = {}
game_min_dict = {}
for slot in gameSlots:
    game_max_dict[slot[0]] = slot[1]
    game_min_dict[slot[0]] = slot[2]

# change practiceslots variable into a dict
practice_max_dict = {}
practice_min_dict = {}
for slot in practiceSlots:
    practice_max_dict[slot[0]] = slot[1]
    practice_min_dict[slot[0]] = slot[2]

initial_game_input = {}
initial_practice_input = {}
for part_assign in partialAssignments:
    if checks.is_practice(part_assign[0]):
        if part_assign[1] in initial_practice_input:
            initial_practice_input[part_assign[1]].append(part_assign[0])
        else:
            initial_practice_input[part_assign[1]] = [ part_assign[0] ]
    else:
        if part_assign[1] in initial_game_input:
            initial_game_input[part_assign[1]].append(part_assign[0])
        else:
            initial_game_input[part_assign[1]] = [ part_assign[0] ]

print(initial_game_input)
print(initial_practice_input)

and_tree = Tree(Node(initial_game_input, initial_practice_input, None))

a_tree(and_tree.root)
