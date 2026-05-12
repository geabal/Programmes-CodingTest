def solution(m, n, puddles):
    MOD = 1000000007
    dp = [[0]*m for _ in range(n)]
    # dp에 puddle 표시
    for a,b in puddles:
        dp[b-1][a-1] = -1
    # 시작점의 경로 수는 1개
    dp[0][0] = 1
    # dp로 각 칸에 도달하는 경로 수 계산
    for y in range(n):
        for x in range(m):
            if dp[y][x] == -1:  # 현재 칸이 peddel인 경우
                continue
                
            if x == 0 and y == 0:
                continue
            elif x == 0:
                if dp[y-1][x] != -1:    #이전 칸이 puddle이 아닌 경우
                    dp[y][x] = dp[y-1][x] % MOD
            elif y == 0:
                if dp[y][x-1] != -1:    #이전 칸이 puddle이 아닌 경우
                    dp[y][x] = dp[y][x-1] % MOD
            else:
                if dp[y-1][x] != -1:    # 윗 칸이 puddle이 아닌 경우
                    dp[y][x] = dp[y-1][x] % MOD
                if dp[y][x-1] != -1:    # 왼쪽 칸이 puddle이 아닌 경우
                    dp[y][x] += dp[y][x-1] % MOD
                    
    answer = dp[n-1][m-1] % MOD
    return answer