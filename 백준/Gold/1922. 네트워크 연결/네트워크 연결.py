import sys

input = sys.stdin.readline

class solution:
    def __init__(self, n, m, edge):
        self.n = n
        self.m = m
        self.edge = edge
        self.par = [i for i in range(n+1)]
        self.edge = sorted(self.edge)

    def getpar(self, child):
        if self.par[child] == child:
            return child
        else:
            self.par[child] = self.getpar(self.par[child])
            return self.par[child]
    def union(self, x, y):
        x = self.getpar(x)
        y = self.getpar(y)
        if x<= y:
            self.par[y] = x
        else:
            self.par[x] = y
        return
    def solve(self):
        ans = 0
        connected = 0
        #최소 스패닝 트리
        for cost, s, e, in self.edge:
            if self.getpar(s) != self.getpar(e):
                self.union(s, e)
                ans+= cost
                connected+=1
            #최소 스패닝 트리가 되었는지 확인
            if connected == n-1:
                break
        return ans

n = int(input())
m = int(input())
edge = []
for _ in range(m):
    s, e, cost = map(int, input().split())
    edge.append([cost, s, e])

sol = solution(n, m, edge)
print(sol.solve())