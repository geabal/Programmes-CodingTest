def solution(n, tops):
    div = 10007
    dp = [0]*n
    dp_con = [0]*n  #밑변이 평행사변형꼴로 끝났을 경우
    if tops[0] == 1:
        dp[0] = 4
        dp_con[0] = 3
    else:
        dp[0] = 3
        dp_con[0] = 2
    
    for i in range(1, n):
        sep_case = 0    # 이전 부분과 분리된 모양인 경우
        con_case = 0    # 마지막 부분이 평행사변형 모양으로 끝나는 경우
        if tops[i] == 1:
            sep_case = 3
            con_case = 2
        else:
            sep_case = 2
            con_case = 1
        
        dp[i] = (dp[i-1] * sep_case + dp_con[i-1]) % div
        dp_con[i] = (dp[i-1]*con_case + dp_con[i-1]) % div
    
    return dp[-1]