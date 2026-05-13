from collections import deque

def solution(n, edge):
    # BFS 순회로 최하단 레벨(리프) 노드 수 세기
    # visit: 노드 방문 여부 저장
    visit = [False]*(n+1)
    # graph = {출발:[도착1, 도착2...],...}
    graph = {}
    #양방향 간선이므로 양방향으로 edge 정보 추가
    for s, e in edge:
        if s in graph:
            graph[s].append(e)
        else:
            graph[s] = [e]
            
        if e in graph:
            graph[e].append(s)
        else:
            graph[e] = [s]
    
    #BFS 순회
    q = deque()
    q.append(1)
    visit[1] = True
    leaf_num = 1
    while q:
        #다음에 방문할 수 있는 노드 리스트 queue에 추가
        for _ in range(leaf_num):
            par = q.popleft()
            candi = graph[par]
            #방문하지 않은 노드만 다음에 방문할 노드로 추가
            for c in candi:
                if visit[c]==False:
                    q.append(c)
                    visit[c] = True
        #부모 노드가 모두 제거되고 자식 노드만 남았을 때 leaf node 수 세기
        if len(q)==0:
            # 마지막 leaf node까지 순회가 끝난 경우, 최종 leaf_num을 결과로 반환
            break
        else:
            leaf_num = len(q)
    
    answer = leaf_num
    return answer