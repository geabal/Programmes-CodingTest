class Puzzle:
    def __init__(self, d, t, l):
        self.diffs = d
        self.times = t
        self.limit = l
        self.level = 0
        
    def setlevel(self, l):
        self.level = l
    
    def solve(self):
        time_prev = 0  
        time_whole = 0  #전체 소요 시간
        
        for i, diff in enumerate(self.diffs):
            time_cur = self.times[i]
            if diff <= self.level:
                time_whole += time_cur
            else:
                tmp = (diff- self.level)*(time_cur+time_prev) + time_cur
                time_whole += tmp
            time_prev = time_cur

            if time_whole > self.limit:
                return False
            
        return True

def solution(diffs, times, limit):
    answer = 0
    minl, maxl = 1, 100000
    mid = (minl + maxl)//2
    pz = Puzzle(diffs, times, limit)
    pz.setlevel(mid)
    isSolve = False
    while maxl-minl > 1:
        isSolve = pz.solve()
        if isSolve:
            maxl = mid
            mid = (minl + maxl)//2
        else:
            minl = mid
            mid = (minl + maxl)//2
        pz.setlevel(mid)
    
    isSolve = pz.solve()
    if isSolve:
        answer = mid
    else:
        answer = mid + 1
        
    return answer