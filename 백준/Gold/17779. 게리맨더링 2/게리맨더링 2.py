def getcase(N):
    d1, d2 = 1,1
    x, y = 0, 0
    cases = []

    for i in range(N):
        for j in range(N):
            x, y = i, j
            for k1 in range(1,N):
                for k2 in range(1, N-k1):
                    d1, d2 = k1, k2
                    if x +d1 +d2 < N and 0 <= y-d1 and y+d2 < N:
                        cases.append([x,y,d1,d2])

    return cases
def solve():
    ans = float('inf')
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]

    cases = getcase(N)
    for x, y, d1, d2 in cases:
        PopulofArea = [0]*6
        board = [[5]*N for _ in range(N)]

        #구역 나누기
        for i in range(d2):
            board[x+i][y+i] = -1
            board[x+d1+i][y-d1+i] = -1
        for i in range(d1+1):
            board[x+i][y-i] = -1
            board[x+d2+i][y+d2-i] = -1

        for i in range(x+d1):
            for j in range(y+1):
                if board[i][j] == -1:
                    break
                board[i][j] = 1
        for i in range(x+d2+1):
            for j in range(N-1, y, -1):
                if board[i][j] == -1:
                    break
                board[i][j] = 2
        for i in range(x+d1, N):
            for j in range(y-d1+d2):
                if board[i][j] == -1:
                    break
                board[i][j] = 3
        for i in range(x+d2+1, N):
            for j in range(N-1,y-d1+d2-1,-1):
                if board[i][j] == -1:
                    break
                board[i][j] = 4

        #구역별 인구수 합산
        for i in range(N):
            for j in range(N):
                PopulofArea[board[i][j]] += A[i][j]

        #인구 수 차이 최대값 확인
        ans = min(ans, max(PopulofArea[1:])-min(PopulofArea[1:]))

    return ans

print(solve())
