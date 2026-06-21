import sys
 
sys.setrecursionlimit(1000000)

class DFS:
    ans_e = -1
    ans_s = -1
    direc = [[0,1], [1,0], [-1,0],[0,-1]]
    def __init__(self, s, e, l, maps): #s, e는 [x,y] 좌표 순서로 입력 받음.
        # 시작, 끝 좌표 입력 받음
        self.start = s
        self.end = e
        self.lever = l
        self.maps = maps
        self.width, self.height = len(maps[0]), len(maps)
        self.visit = [[float('inf')]*self.width for _ in range(self.height)]
        self.visit[l[1]][l[0]] = 0
        return
    
    def dfs(self, par, dist):
        for xi, yi in self.direc:
            now_x = par[0] + xi
            now_y = par[1] + yi
            #이동 가능한 곳 좌표 찾기
            if (0<=now_x<self.width) and (0<= now_y<self.height) and (self.maps[now_y][now_x] !='X') and (self.visit[now_y][now_x] > dist):
                self.visit[now_y][now_x] =dist
                
                if now_x == self.end[0] and now_y == self.end[1]:
                    if self.ans_e == -1:
                        self.ans_e = dist
                    else:
                        self.ans_e = min(dist, self.ans_e)

                elif now_x == self.start[0] and now_y == self.start[1]:
                    if self.ans_s == -1:
                        self.ans_s = dist
                    else:
                        self.ans_s = min(dist, self.ans_s)
                    
                
                self.dfs([now_x,now_y], dist+1)

        return

def solution(maps):
    #l, s, e 위치 찾기
    l, s, e = [0,0],[0,0],[0,0]
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'L':
                l = [j, i]
            if maps[i][j] == 'S':
                s = [j, i]
            if maps[i][j] == 'E':
                e = [j, i]
                
    ltose = DFS(s, e, l, maps)
    ltose.dfs(l, 1)
    if ltose.ans_e == -1 or ltose.ans_s == -1:
        return -1

    return (ltose.ans_e + ltose.ans_s )
    