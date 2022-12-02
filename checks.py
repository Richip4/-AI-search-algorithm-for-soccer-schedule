from main import *  # super bad practice just avert your eyes

def check_hard_constraints(node):
    pass


def check_soft_constraints(node):
    pass


def is_complete_schedule(node):
    for game in games:
        is_in_some_slot = False
        for slot in node.schedule:
            if node.schedule[slot] == game:
                is_in_some_slot = True # check off this game
                break
        if not is_in_some_slot:
            return False

    for practice in practices:
        is_in_some_slot = False
        for slot in node.schedule:
            if node.schedule[slot] == practice:
                is_in_some_slot = True # check off this game
                break
        if not is_in_some_slot:
            return False

    return True
