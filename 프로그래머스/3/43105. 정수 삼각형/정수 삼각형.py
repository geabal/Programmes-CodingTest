from copy import deepcopy
def solution(triangle):
    dp = deepcopy(triangle)
    depth = len(triangle)
    
    for d in range(1,depth):
        for i, n in enumerate(dp[d]):
            if i == 0:
                dp[d][i] += dp[d-1][i]
            elif i == len(dp[d])-1:
                dp[d][i] += dp[d-1][i-1]
            else:
                dp[d][i] += max(dp[d-1][i], dp[d-1][i-1])
    
    return max(dp[-1])