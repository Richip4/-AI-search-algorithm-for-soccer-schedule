from main import *  # super bad practice just avert your eyes

def check_hard_constraints(node):
    for slot in node.game_schedule:
        if len(node.game_schedule[slot]) > game_max_dict[slot]:
            return False

        for bad_pair in notCompatible:
            if bad_pair[0] in node.game_schedule[slot] and bad_pair[1] in node.game_schedule[slot]:
                return False

    for slot in node.practice_schedule:
        if len(node.practice_schedule[slot]) > practice_max_dict[slot]:
            return False
        # minimums are checked in check_save once the schedule is complete

        for bad_pair in notCompatible:
            if bad_pair[0] in node.practice_schedule[slot] and bad_pair[1] in node.practice_schedule[slot]:
                return False

    # check nocompat same division
    for p_slot in node.practice_schedule:
        for g_slot in colliding_games:
            if (node.practice_schedule[p_slot].league == node.game_schedule[g_slot].league and
                    (node.practice_schedule[p_slot].division == 0 or
                     node.practice_schedule[p_slot].division == node.game_schedule[g_slot].division)):
                return False # this code is wrong

    # not partassign
    # unwanted assigned to each other
    # div9+ not scheduled after 18:00
    # u15 16 17 19 overlap slots
    # if game is booked at tuesday 11-1230h
    # u12t1s & u13t1s must be on tuesday 18-1900h
    # if there is a booking for u12t1 or u13t1:
    #   u12t1s cannot overlap u12t1,
    #   u13t1s """""""""""""" u13t1


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

def is_practice(str):
    if "PRC" in str or "OPN" in str:
        return True
    return False
