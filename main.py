from parser import parser
from and_tree import *
from checks import *

def a_tree(node):
    # if all children are solved then solve yourself & move up
    if not check_hard_constraints(node):
        node.solved = True
        node = node.parent
    elif is_complete_schedule(node):
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
    score = check_soft_constraints(node)
    global best_score
    if score < best_score:
        global best_node
        best_node = node
        best_score= score

gameSlots, practiceSlots, games, practices, notCompatible, unwanted, preferences, pair, partialAssignments = parser()

initial_input = {}
for part_assign in partialAssignments:
    if part_assign[1] in initial_input:
        initial_input[part_assign[1]].append(part_assign[0])
    else:
        initial_input[part_assign[1]] = [ part_assign[0] ]

and_tree = Tree(Node(initial_input, None))

a_tree(and_tree.root)
