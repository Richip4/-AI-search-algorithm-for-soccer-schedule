def minFilled(aNode, penGameMin, penPracticeMin):
    gameSchedule = aNode.game_schedule
    eval = 0
    for i in list(gameSchedule.keys()):
        if (len(gameSchedule[i]) < i.sessionMin):
            diff = i.sessionMin - len(gameSchedule[i])
            pen = diff * penGameMin
            eval = eval + pen
    
    practiceSchedule = aNode
    for i in list(practiceSchedule.keys()):
        if (len(practiceSchedule[i]) < i.sessionMin):
            diff = i.sessionMin - len(practiceSchedule[i])
            pen = diff * penPracticeMin
            eval = eval + pen 
    
    return eval


def pair(aNode, pairs, penNotPair):
    gameSchedule = aNode.game_schedule
    isIn = False
    eval = 0
    for i in list(gameSchedule.keys()):
        for a in gameSchedule[i]:
            for b in pairs:
                if(a in b):
                    for c in aNode.practice_schedule[i]:
                        if(c != a and c in b):
                            isIn = True
                
                if(isIn == False):
                    eval = eval + penNotPair
                
                isIn = False
    
    return eval 
        