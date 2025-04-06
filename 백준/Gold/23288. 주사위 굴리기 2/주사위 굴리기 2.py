from collections import deque
class Dice:
    def __init__(self):
        self.__dice = [6, 5, 1, 4, 3, 2]  # down front up left right back
        self.__dy = [1, 0, -1, 0]  # 동 남 서 북
        self.__dx = [0, 1, 0, -1]
        self.__direc = 0
    def roll(self):
        if self.__direc == 0:
            self.roll_right()
        elif self.__direc == 1:
            self.roll_down()
        elif self.__direc == 2:
            self.roll_left()
        else:
            self.roll_up()
    def roll_right(self):
        # [3, 5, 4, 6, 1, 2]
        tmp = self.__dice[0]
        self.__dice[0] = self.__dice[4]
        self.__dice[4] = self.__dice[2]
        self.__dice[2] = self.__dice[3]
        self.__dice[3] = tmp
    def roll_left(self):
        #[4,5,3,1,6,2]
        tmp = self.__dice[0]
        self.__dice[0] = self.__dice[3]
        self.__dice[3] = self.__dice[2]
        self.__dice[2] = self.__dice[4]
        self.__dice[4] = tmp
    def roll_up(self):
        #[2, 6, 5, 4, 3, 1]
        tmp = self.__dice[0]
        self.__dice[0] = self.__dice[5]
        self.__dice[5] = self.__dice[2]
        self.__dice[2] = self.__dice[1]
        self.__dice[1] = tmp
    def roll_down(self):
        #[5, 1, 2, 4, 3, 6]
        tmp = self.__dice[0]
        self.__dice[0] = self.__dice[1]
        self.__dice[1] = self.__dice[2]
        self.__dice[2] = self.__dice[5]
        self.__dice[5] = tmp

    def getDown(self):
        return self.__dice[0]
    def getDirec(self):
        return self.__direc, self.__dx[self.__direc], self.__dy[self.__direc]
    def setDirec(self, B):
        A = self.__dice[0]
        if A > B:
            if self.__direc == 3:
                self.__direc = 0
            else:
                self.__direc += 1
        elif A < B:
            if self.__direc == 0:
                self.__direc = 3
            else:
                self.__direc -= 1

    def reverseDirec(self):
        if self.__direc > 1:
            self.__direc -= 2
        else:
            self.__direc += 2

def solve():
    N, M, K = list(map(int, input().split()))
    board = [list(map(int, input().split())) for _ in range(N)]
    scoreBoard = [[0] * M for _ in range(N)]
    ans = 0
    dice = Dice()
    cx, cy = 0, 0
    #K번 주사위 굴리기
    for _ in range(K):
        cdirec, dx, dy = dice.getDirec()
        nx, ny = cx + dx, cy + dy
        if not (0 <= nx < N and 0 <= ny < M):
            dice.reverseDirec()
            cdirec, dx, dy = dice.getDirec()
            nx, ny = cx + dx, cy + dy
        cx, cy = nx, ny
        dice.roll() #주사위 굴리기
        B = board[cx][cy]   # 주사위가 올려진 보드 위치 값
        dice.setDirec(B)    # 주사위 이동 방향 변화

        # 점수 합산
        q = deque()
        if scoreBoard[cx][cy] == 0: #bfs
            dc = [0,0,1,-1]
            dr = [1,-1,0,0]
            q.append([cx, cy])
            cnt = 1
            scoreBoard[cx][cy] = -1
            while q:
                tx, ty = q.popleft()
                for i in range(4):
                    nx, ny = tx + dc[i], ty+dr[i]
                    if 0<= nx < N and 0<= ny < M and scoreBoard[nx][ny] == 0 and board[nx][ny] == B:
                        q.append([nx,ny])
                        scoreBoard[nx][ny] = -1
                        cnt += 1

            score = B * cnt
            for i in range(N):
                for j in range(M):
                    if scoreBoard[i][j] == -1:
                        scoreBoard[i][j] = score

        ans += scoreBoard[cx][cy]
    return ans

print(solve())