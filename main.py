from parser import parser


def main():
    print("hello world!!")

'''def tree_search(initial_problem_state, search_strategy):
    # initialize search tree using initial state of the problem
    while True:
        if there are no candidates for expansion:
            return False
        node = search_strategy.get_node_for_expansion() # choose a leaf node according to the search_strategy
        if node.contains_goal_state():
            return solution
        else:
            node.expand()
            child_nodes = node.children
            add_to_search_tree(child_nodes)'''

gameSlots, practiceSlots, games, practices, notCompatible, unwanted, preferences, pair, partialAssignments = parser()

'''print("games slot:", gameSlots)
print("practice slot:", practiceSlots)
print("games:", games)
print("practices:", practices)
print("not compatible:", notCompatible)
print("unwanted:", unwanted)
print("preferences:", preferences)
print("pair:", pair)
print("partial assignments:", partialAssignments)'''

initial_input = {}
for part_assign in partialAssignments:
    if part_assign[1] in initial_input:
        initial_input[part_assign[1]].append(part_assign[0])
    else:
        initial_input[part_assign[1]] = [ part_assign[0] ]


print("dictionary: ", initial_input)
