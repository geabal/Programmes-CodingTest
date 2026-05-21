def solution(s):
    answer = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if s[i:j] == s[i:j][::-1]:
                answer = max(answer, len(s[i:j]))
    return answer

# def solution(s):
    
    
#     #홀수 팰린드롬
#     dp1 = [1]*len(s)
    
#     for i, ch in enumerate(s):
#         start, end = i -1, i + 1
#         while -1 < start and end < len(s):
#             if s[start] == s[end]:
#                 dp1[i] += 2
#             start -= 1
#             end += 1
        
#     #짝수 팰린드롬
#     dp2 = [0]*len(s)
#     for i in range(len(s)-1):
#         start, end = i, i + 1
#         while -1 < start and end < len(s):
#             if s[start] == s[end]:
#                 dp2[i] += 2
#             start -= 1
#             end += 1
#     print(dp1, dp2)
#     answer = max(max(dp1), max(dp2))

#     return answer