# from main import *
import copy


def check_hard_constraints(node, notCompatible, unwanted, eveningGameSlots, eveningPracticeSlots):
    for slot in list(node.game_schedule.keys()):

        # check game max... min checked in check_save
        if len(node.game_schedule[slot]) > slot.sessionMax:
            return False

        # cannot have a game at TU 11:00
        if slot.day == "TU" and slot.time == 1100:
            if len(node.game_schedule[slot]) > 0:
                return False

        over_u15 = 0  # checks games in u15+ that are overlapping
        for session in node.game_schedule[slot]:
            # u15+ games can't overlap
            if ("U15" in session.league) or ("U16" in session.league) or ("U17" in session.league) or (
                    "U19" in session.league):
                over_u15 = over_u15 + 1
                if over_u15 > 1:
                    return False

            # check div 9 evening slot
            if session.division >= 9 and not (slot in eveningGameSlots):
                return False

            # check if unwanted game is set
            for not_wanted in unwanted:
                #if ((session.league + " DIV " + str(session.division)) in not_wanted[0]) and (not_wanted[1].replace(":", "") == slot.day + " " + str(slot.time)):
                #print("session name" + session.fullname + "not wanted" + not_wanted[0])
                if ((session.fullname == not_wanted[0]) and (slot.day == not_wanted[1][0:2]) and (str(slot.time) == not_wanted[1][3:].replace(":", "")) ):
                    #print("retruns FALSE")
                    return False

            # check not compatible games are set to each other
            for bad_pair in notCompatible:
                if (session.league + " DIV " + str(session.division)) in bad_pair[0]:
                    for session2 in node.game_schedule[slot]:
                        if (session2.league + " DIV" + str(session2.division)) in bad_pair[1]:
                            return False

    # practices below
    # for when special t1s practices are requested
    # if there is a booking for u12t1 or u13t1:
    u13t1s_requested = False
    u12t1s_requested = False
    for slot in list(node.practice_schedule.keys()):
        for session in node.practice_schedule[slot]:
            if "U13T1S" in session.league:
                u13t1s_requested = True
            elif "U12T1S" in session.league:
                u12t1s_requested = True
            # u12t1s & u13t1s must be on tuesday 18-1900h

            if (("U13T1S" in session.league) or ("U12T1S" in session.league)) and (
                    (slot.day != "TU") or (slot.time != 1800)):
                return False

            # check practice max
            if len(node.practice_schedule[slot]) > slot.sessionMax:
                return False
            # minimums are checked in soft once the schedule is complete

            # check div 9 evening slot
            if session.division >= 9 and not (slot in eveningPracticeSlots):
                return False

            # check if unwanted game is set
            for not_wanted in unwanted:
                #if (session.fullname == not_wanted[0]) and (not_wanted[1].replace(":", "") == slot.day + " " + slot.time):
                if ((session.fullname == not_wanted[0]) and (slot.day == not_wanted[1][0:2]) and (str(slot.time) == not_wanted[1][3:].replace(":", ""))):  
                    return False

            for bad_pair in notCompatible:
                if session.fullname == bad_pair[0]:
                    for session2 in node.practice_schedule[slot]:
                        if session2.fullname == bad_pair[1]:
                            return False

        #THIS WORKS NOW BUT COMMENTED OUT THE FIRST IF
        #   u12t1s cannot overlap u12t1,
        #   u13t1s """""""""""""" u13t1
        for session in node.practice_schedule[slot]:
            for session2 in node.practice_schedule[slot]:
                # if (session.league == session2.league) and (session.division == session2.division):
                #     return False
                # check if t1 in session then check other sessions to see if duplicate, then go to next session
                if ("U13T1 " in (session.league + " ")) and ("U13T1S " in (session2.league + " ")) or \
                        ("U12T1 " in (session.league + " ")) and ("U12T1S " in (session2.league + " ")):
                    return False

    # over lapping part
    for g_slot in node.game_schedule:
        for p_slot in node.practice_schedule:
            if overlapping(g_slot, p_slot):
                for g_session in node.game_schedule[g_slot]:
                    for p_session in node.game_schedule[p_slot]:
                        # u12t1s cant overlap
                        if (u12t1s_requested and ("U12T1" in g_session.league) and ("U12T1S" in p_session)) or (
                                u13t1s_requested and ("U13T1" in g_session.league) and ("U13T1S" in p_session)):
                            return False

                        # check nocompat same division
                        if (g_session.league == p_session.league) and ((p_session.division == 0) or
                                                                       (g_session.division == p_session.division)):
                            return False
    return True

    # not partassign (dont need to check this since all partassign are assigned at the start) ignore


def overlapping(game_slot, practice_slot):
    if (game_slot.day == "MO") and (practice_slot == "FR") and ((game_slot.time == practice_slot.time) or (
            game_slot.time == practice_slot.time + 100)):
        return True

    elif game_slot.day != practice_slot.day:
        return False

    elif (game_slot.day == "MO") and (practice_slot == "MO") and (game_slot.time == practice_slot.time):
        return True  # monday slots are the same for both prac and game

    elif (game_slot.day == "TU") and (practice_slot == "TU"):
        if (game_slot.day % 100 == 30) and ((game_slot.time - 30 == practice_slot.time) or (
                game_slot.time + 70 == practice_slot.time)):
            return True
        elif (game_slot.day % 100 == 0) and ((game_slot.time == practice_slot.time) or (
                game_slot.time + 100 == practice_slot.time)):
            return True
    else:
        return False


def check_soft_constraints(node, pref, penGameMin, penPracticeMin, pairs, penNotPair, penSecdiff, wMinFill, wPref, wPair, wSecDiff):
    # min penalty
    gameSchedule = node.game_schedule
    min_eval = 0
    for i in list(gameSchedule.keys()):
        if (len(gameSchedule[i]) < i.sessionMin):
            diff = i.sessionMin - len(gameSchedule[i])
            pen = diff * penGameMin
            min_eval = min_eval + pen

    practiceSchedule = node.practice_schedule
    for i in list(practiceSchedule.keys()):
        if (len(practiceSchedule[i]) < i.sessionMin):
            diff = i.sessionMin - len(practiceSchedule[i])
            pen = diff * penPracticeMin
            min_eval = min_eval + pen

    pref_eval = 0
    # pref soft constraint
    for slot in node.game_schedule:
        for session in node.game_schedule[slot]:
            for pref_slot in pref:
                if session.fullname in pref_slot:
                    if slot.day + " " + str(slot.time) != pref_slot[0].replace(":", ""):
                        pref_eval = pref_eval + int(pref_slot[2])

    for slot in node.practice_schedule:
        for session in node.practice_schedule[slot]:
            for pref_slot in pref:
                if session.fullname in pref_slot:
                    if slot.day + " " + str(slot.time) != pref_slot[0].replace(":", ""):
                        pref_eval = pref_eval + int(pref_slot[2])


    # pair penalty
    gameSchedule = node.game_schedule
    isIn = False
    pair_eval = 0
    for i in list(gameSchedule.keys()):
        for a in gameSchedule[i]:
            for b in pairs:
                if (a in b):
                    for c in node.practice_schedule[i]:
                        if (c != a and c in b):
                            isIn = True

                if (isIn == False):
                    pair_eval = pair_eval + penNotPair

                isIn = False

    # secdiff soft constraint
    secdiff_eval = 0
    for slot in node.game_schedule:
        checked_sess = ""
        for session in node.game_schedule[slot]:
            if checked_sess == session.league:
                continue
            for session2 in node.game_schedule[slot]:
                if (session.league == session2.league) and (session.division != session2.division):
                    checked_sess = session.league
                    secdiff_eval = secdiff_eval + penSecdiff
                    break
    print(secdiff_eval)

    eval = min_eval*wMinFill + pref_eval*wPref + pair_eval*wPair + secdiff_eval*wSecDiff
    return eval


def is_complete_schedule(node, games, practices):
    for game in games:
        is_in_some_slot = False
        for slot in node.game_schedule:
            for session in node.game_schedule[slot]:
                if session.fullname == game.fullname:
                    is_in_some_slot = True  # check off this game
                    break
            if is_in_some_slot:
                break
        if not is_in_some_slot:
            return False

    for practice in practices:
        is_in_some_slot = False
        for slot in node.practice_schedule:
            for session in node.practice_schedule[slot]:
                if session.fullname == practice.fullname:
                    is_in_some_slot = True  # check off this game
                    break
            if is_in_some_slot:
                break
        if not is_in_some_slot:
            return False

    return True


def is_practice(string):  # should take a game and return isPractice boolean from object
    if "PRC" in string or "OPN" in string:
        return True
    return False
