def solution(n, money):
    MOD = 1_000_000_007
    #dp[i]: 현재 동전으로 i원을 만들 수 있는 경우의 수
    dp = [0]*(n+1)
    #0원을 만드는 방법 수는 1개(동전을 쓰지 않는 것)
    dp[0] = 1
    #dp[i] = dp[i]+dp[i-coin]
    
    for coin in money:
        for i in range(coin, n+1):
            dp[i] = (dp[i] +dp[i-coin]) % MOD

    return dp[n]