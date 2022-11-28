def main():
    print("hello world!!")

def tree_search(initial_problem_state, search_strategy):
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
            add_to_search_tree(child_nodes)