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

    def __str__(self):
        return "league: " + str(self.league) + ", division: " + str(self.division) + ", practice?: " + str(self.is_practice)

class Slot:

    def __init__(self, d, t, mx, mn, prac):
        self.day = d
        self.time = t
        self.sessionMax = mx
        self.sessionMin = mn
        self.isPractice = prac

    def __str__(self):
        return self.day + ", time: " + str(self.time) + ", max: " + str(self.sessionMax) + ", min: " + str(self.sessionMin) + ", practice? = " + str(self.isPractice)
