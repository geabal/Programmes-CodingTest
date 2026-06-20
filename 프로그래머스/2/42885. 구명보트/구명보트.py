from collections import deque
def solution(people, limit):
    answer = 0
    #몸무게 내림차순으로 sort
    sorted_p = deque(sorted(people, reverse=True))
    
    while sorted_p:
        heavy, light = sorted_p[0], sorted_p[-1]
        if heavy+light <= limit:
            sorted_p.popleft()
            if sorted_p:    
                # 마지막에 한 사람만 남은 경우, sorted_p가 빌 수 있음. 
                # sorted_p에 요소가 있는 경우에만 pop
                sorted_p.pop()
        else:
            sorted_p.popleft()
        answer += 1
    
    return answer