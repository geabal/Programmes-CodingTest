from heapq import heappop, heappush
from collections import defaultdict

def solution(N, road, K):
    # graph = {출발점:[[도착점1,시간1],...],...}
    graph = defaultdict(list)
    cost = [[float('inf')]*(N+1) for _ in range(N+1)]
    for a, b, time in road:
        #양방향 간선 기록
        graph[a].append([b,time])
        graph[b].append([a,time])
        cost[a][b] = time
        cost[b][a] = time
    
    #다익스트라 구현
    #dists: 시작점(1)과 떨어진 거리 기록
    dists = [float('inf')]*(N+1)
    dists[1] = 0
    q = [[0,1]]
    while q:
        cur_dist, cur_node = heappop(q)
        if cur_dist > dists[cur_node]:  #이전에 기록했던 거리보다 큰 경로는 순회 x
            continue
        
        children = graph[cur_node]
        for next_node, time in children:
            if cur_dist + time < dists[next_node]:
                dists[next_node] = cur_dist + time
                heappush(q, [dists[next_node], next_node])
    
    answer = 0
    
    #배달 시간이 K 이하인 것 개수 세기
    for dist in dists:
        if dist <= K:
            answer += 1

    return answer