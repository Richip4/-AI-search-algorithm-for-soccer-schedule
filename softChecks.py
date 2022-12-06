def minFilled(aNode, penGameMin, penGameMax):
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
            pen = diff * penGameMin
            eval = eval + pen 
    
    return eval