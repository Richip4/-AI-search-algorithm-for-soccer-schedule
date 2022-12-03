#from main import notCompatible
import copy


def check_hard_constraints(node, notCompatible):
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
    for g_slot in node.game_schedule:
        for p_slot in overlapping_practices(g_slot):
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

def overlapping_practices(game_slot):
    if "MO" in game_slot:
        return game_slot
    slot = copy.copy(game_slot)
    slot = slot[3:]             # strip day of the week from the string
    if slot == "8:00":
        return eanrsoeitnars
    elif slot == "9:00":
        return aienrsoten
    elif slot == "10:00":
        return erinstoaienrst

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

def is_practice(string):
    if "PRC" in string or "OPN" in string:
        return True
    return False
