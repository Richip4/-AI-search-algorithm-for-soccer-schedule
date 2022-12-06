class Node:
    # game_schedule = {}
    # practice_schedule = {}
    # children = []
    # parent = None
    # solved = False

    def __init__(self, games, practices, parent, children):
        self.game_schedule = games
        self.practice_schedule = practices
        self.parent = parent
        self.children = children
        self.solved = False

class Tree:
    root = None
    solved = False

    def __init__(self, root):
        self.root = root

class Session:
    league = ""         # example: CSMA U17T1
    division = 0        # example: 1
    is_practice = False

    def __init__(self, l, d, p):
        self.league = l
        self.division = d
        self.is_practice = p

    def __str__(self):
        return str(self.league) + " " + str(self.division) + " " + str(self.is_practice)


node1 = Node(None, None, None)
node1.children.append(5)
node2 = Node(None, None, None)
node2.children.append(10)

print(node1 == node2)
print(node2.children)