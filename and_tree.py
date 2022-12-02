class Node:
    element = {}
    children = []
    parent = None
    solved = False

    def __init__(self, element, parent):
        self.element = element
        self.parent = parent

class Tree:
    root = None
    solved = False

    def __init__(self, root):
        self.root = root
