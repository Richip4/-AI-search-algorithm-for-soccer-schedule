class Node:
    game_schedule = {}
    practice_schedule = {}
    children = []
    parent = None
    solved = False

    def __init__(self, games, practices, parent):
        self.game_schedule = games
        self.practice_schedule = practices
        self.parent = parent

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

    def __init__(self, l, p):
        self.league = l
        self.is_practice = p
