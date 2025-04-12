class Monomino:
    def __init__(self):
        self.bboard = [[0] * 6 for _ in range(4)]
        self.gboard = [[0] * 4 for _ in range(6)]
        self.score = 0
        self.blast = -1 #파란색 보드에서 가장 최근에 블럭이 놓인 열(가장안쪽)
        self.glast = -1 #초록색 보드에서 가장 최근에 블럭이 놓인 행(가장안쪽)

    def __add1(self, x, y):
        #파란 보드에 블럭 놓기
        for i in range(1,5):
            if self.bboard[x][i + 1] == 0:
                if i == 4:
                    self.bboard[x][5] = 1
                    self.blast = 5
                continue
            else:
                self.bboard[x][i] = 1
                self.blast = i
                break
        #초록 보드에 블럭 놓기
        for i in range(1,5):
            if self.gboard[i+1][y] == 0:
                if i == 4:
                    self.gboard[5][y] = 1
                    self.glast = 5
                continue
            else:
                self.gboard[i][y] = 1
                self.glast = i
                break
    def __add2(self, x, y):
        # 파란 보드에 블럭 놓기
        for i in range(1, 5):
            if self.bboard[x][i + 1] == 0:
                if i == 4:
                    self.bboard[x][4] = 1
                    self.bboard[x][5] = 1
                    self.blast = 5
                continue
            else:
                self.bboard[x][i-1] = 1
                self.bboard[x][i] = 1
                self.blast = i
                break
        # 초록 보드에 블럭 놓기
        for i in range(1, 5):
            if self.gboard[i + 1][y] == 0 and self.gboard[i + 1][y+1] == 0 :
                if i == 4:
                    self.gboard[5][y] = 1
                    self.gboard[5][y+1] = 1
                    self.glast = 5
                continue
            else:
                self.gboard[i][y] = 1
                self.gboard[i][y+1] = 1
                self.glast = i
                break
    def __add3(self, x, y):
        # 파란 보드에 블럭 놓기
        for i in range(1, 5):
            if self.bboard[x][i + 1] == 0 and self.bboard[x+1][i + 1] == 0:
                if i == 4:
                    self.bboard[x][5] = 1
                    self.bboard[x+1][5] = 1
                    self.blast = 5
                continue
            else:
                self.bboard[x][i] = 1
                self.bboard[x+1][i] = 1
                self.blast = i
                break
        # 초록 보드에 블럭 놓기
        for i in range(1, 5):
            if self.gboard[i + 1][y] == 0:
                if i == 4:
                    self.gboard[4][y] = 1
                    self.gboard[5][y] = 1
                    self.glast = 5
                continue
            else:
                self.gboard[i-1][y] = 1
                self.gboard[i][y] = 1
                self.glast = i
                break

    def erase(self, color, num):
        if color == 'b':
            for k in range(4):
                self.bboard[k][num] = 0
        else:
            for k in range(4):
                self.gboard[num][k] = 0

    def pullBlock(self, color, erased):
        if not erased:
            return
        gap = len(erased)
        if color == 'b':
            for i in range(erased[-1], gap-1, -1):
                for j in range(4):
                    self.bboard[j][i] = self.bboard[j][i-gap]
            for i in range(gap):
                self.erase('b', i)

        else:
            for i in range(erased[-1], gap-1, -1):
                for j in range(4):
                    self.gboard[i][j] = self.gboard[i-gap][j]
            for i in range(gap):
                self.erase('g', i)


    def scorizing(self):
        #파란 보드 스코어 체크
        erased = []
        for i in range(self.blast-1, self.blast+1):
            for j in range(4):
                if self.bboard[j][i] == 0:
                    break
                elif j == 3:
                    self.score += 1
                    self.erase('b', i)
                    erased.append(i)
        self.pullBlock('b',erased)

        # 초록 보드 스코어 체크
        erased = []
        for i in range(self.glast - 1, self.glast + 1):
            for j in range(4):
                if self.gboard[i][j] == 0:
                    break
                elif j == 3:
                    self.score += 1
                    self.erase('g', i)
                    erased.append(i)

        self.pullBlock('g', erased)

    def pushBlock(self):
        # 파란 보드 확인
        needToPush = 0
        for i in range(2):
            for j in  range(4):
                if self.bboard[j][i] == 1:
                    needToPush += 1
                    break
        if needToPush > 0:
            for i in range(5, 1, -1):
                for j in range(4):
                    self.bboard[j][i] = self.bboard[j][i-needToPush]
            self.erase('b', 0)
            self.erase('b', 1)

        # 초록 보드 확인
        needToPush = 0
        for i in range(2):
            for j in range(4):
                if self.gboard[i][j] == 1:
                    needToPush += 1
                    break
        if needToPush > 0:
            for i in range(5, 1, -1):
                for j in range(4):
                    self.gboard[i][j] = self.gboard[i- needToPush][j]
            self.erase('g', 0)
            self.erase('g', 1)

    def add(self, t, x, y):
        #board에 블럭 놓음
        if t == 1:
            self.__add1(x,y)
        elif t ==2:
            self.__add2(x, y)
        else:
            self.__add3(x,y)

        #점수 합산
        self.scorizing()

        #블럭 밀기
        self.pushBlock()

    def getScore(self):
        return self.score
    def getBlockNum(self):
        bn, gn = 0, 0
        for i in range(4):
            bn += self.bboard[i].count(1)
        for i in range(6):
            gn += self.gboard[i].count(1)
        return (bn + gn)

    def printBlock(self):
        print('blue board')
        for i in range(4):
            print(self.bboard[i])
        print('green board')
        for i in range(6):
            print(self.gboard[i])
def solve():
    n = int(input())
    mono = Monomino()
    for _ in range(n):
        t, x, y = list(map(int, input().split()))
        mono.add(t,x,y)
    print(mono.getScore())
    print(mono.getBlockNum())

    return

solve()