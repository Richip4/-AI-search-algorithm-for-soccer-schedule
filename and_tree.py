class Node:
    schedule = {}
    children = []
    parent = None
    solved = False

    def __init__(self, element, parent):
        self.schedule = element
        self.parent = parent

class Tree:
    root = None
    solved = False

    def __init__(self, root):
        self.root = root
<<<<<<< Updated upstream
=======

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
>>>>>>> Stashed changes
