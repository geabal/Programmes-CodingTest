from itertools import product

def solution(word):
    answer = 0
    check = ['A','E','I','O','U']
    checklist = []
    
    for cnt in range(1, 6):
        for i in product(check, repeat=cnt):
            checklist.append(''.join(i))
    
    checklist.sort()
    for idx, val in enumerate(checklist):
        if val == word:
            return idx+1
        
    return answer