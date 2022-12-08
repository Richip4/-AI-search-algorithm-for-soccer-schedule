#class for each node in the And-Tree
class Node:

    def __init__(self, games, practices, parent, children):
        self.game_schedule = games
        self.practice_schedule = practices
        self.parent = parent
        self.children = children
        self.solved = False

#class for the tree itself 
class Tree:
    root = None
    solved = False

    def __init__(self, root):
        self.root = root

#class for each game/practice
class Session:

    def __init__(self, l, d, p, fn):
        self.league = l
        self.division = d
        self.is_practice = p
        self.fullname = fn

    def __str__(self):
        return "league: " + str(self.league) + ", division: " + str(self.division) + ", practice?: " + str(self.is_practice) + ", fullname: " + self.fullname

#class for each time slot 
class Slot:

    def __init__(self, d, t, mx, mn, prac):
        self.day = d
        self.time = t
        self.sessionMax = mx
        self.sessionMin = mn
        self.isPractice = prac

    def __str__(self):
        return self.day + ", time: " + str(self.time) + ", max: " + str(self.sessionMax) + ", min: " + str(self.sessionMin) + ", practice? = " + str(self.isPractice)