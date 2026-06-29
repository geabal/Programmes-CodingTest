import math
def solution(n, stations, w):
    answer = 0
    idx = 1
    for i in stations:
        r1, r2 = i -w, i + w
        if r1 < 1:
            r1  = 1
        if r2 > n:
            r2 = n
        answer += math.ceil((r1 - idx) / (2 * w + 1))
        idx = r2 + 1
    if n >= idx:
        answer += math.ceil((n - idx + 1) / (2 * w + 1))
        
    return answer
        