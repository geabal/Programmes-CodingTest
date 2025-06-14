import sys
from itertools import combinations

input = sys.stdin.readline

class ChickenCalculator:
    def __init__(self, n, m, board):
        self.n = n
        self.m = m
        self.board = board
        self.chickens = []
        self.houses = []
        self.getLoc()   # 치킨집, 집 위치 체크


    def solve(self):
        combs = combinations([x for x in range(len(self.chickens))], self.m)
        min_ans = float('inf')
        for comb in combs:
            ans = 0
            #각 집마다 최소 치킨거리 구하기
            for house in self.houses:
                min_dist = float('inf')
                for c in comb:
                    dist = abs(self.chickens[c][0] - house[0]) + abs(self.chickens[c][1] - house[1])
                    min_dist = min(dist, min_dist)
                ans += min_dist
            min_ans = min(min_ans, ans)

        return min_ans

    def getLoc(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j] == 1:
                    self.houses.append([i, j])
                elif self.board[i][j] == 2:
                    self.chickens.append([i, j])

        return


def Solution():
    n, m = list(map(int, input().split()))
    board = [list(map(int, input().split())) for _ in range(n)]
    cc = ChickenCalculator(n,m,board)

    return cc.solve()

print(Solution())