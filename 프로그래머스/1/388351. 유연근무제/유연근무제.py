def islate(s, tl):
    deadline = s+10
    if (deadline%100) >= 60:
        deadline += (100 - 60)
    if tl <= deadline:
        return False
    else:
        return True

def solution(schedules, timelogs, startday):
    n = len(schedules)
    candi = [True] * n
    
    for i in range(7):
        if startday == 6:
            startday += 1
            continue
        elif startday == 7:
            startday = 1
            continue
        else:
            startday += 1
        
        for j in range(n):
            if candi[j]:
                if islate(schedules[j], timelogs[j][i]):
                    candi[j] = False
    
    return candi.count(True)