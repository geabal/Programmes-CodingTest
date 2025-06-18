from itertools import combinations
def solution(n, q, ans):
    combs = list(combinations(range(1, n+1), 5))
    
    for query, cnt in zip(q, ans):
        combs = [code for code in combs if len(set(code) & set(query)) == cnt]
    
    return len(combs)