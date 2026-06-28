def StealMoney(dp, money): 
    dp[0] = money[0] # 초기값 
    dp[1] = dp[0] # 당연한 값 

    for i in range(2, len(money)): 
        dp[i] = max(dp[i - 1], money[i] + dp[i - 2]) 

    return dp[-2] 

def solution(money): 
    n = len(money) 
    steal1 = StealMoney([0] * n, money) 
    steal2 = StealMoney([0] * n, money[1:] + money[:1]) 
    steal3 = StealMoney([0] * n, money[2:] + money[:2]) 

    return max(steal1, steal2, steal3)
