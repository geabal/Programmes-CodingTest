def solution(n):
    answer = 1
    for a in range(2, n+1):
        k = (n - (a*(a+1))/2)/a
        if k >= 0 and k // 1 == k:
            answer += 1
    
    return answer