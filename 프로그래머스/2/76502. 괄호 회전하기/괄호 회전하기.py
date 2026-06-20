from collections import deque

def isCorrect(d):
    stack = []
    pair = {'[':']', '{':'}', '(':')'}
    for c in d:
        if c == '[' or c == '(' or c == '{':
            stack.append(c)
        else:
            if stack:
                left = stack.pop()
                if pair[left] != c:
                    return False
            else:
                return False
                    
    if stack:
        return False
    else:
        # 순회가 끝나고 스택이 비어있을 경우만 올바른 괄호 문자열로 판별
        return True

def solution(s):
    answer = 0
    d = deque()
    for c in s:
        d.append(c)
    
    if isCorrect(d):
        answer += 1
    for _ in range(len(s)-1):
        left = d.popleft()
        d.append(left)
        if isCorrect(d):
            answer += 1
    
    return answer