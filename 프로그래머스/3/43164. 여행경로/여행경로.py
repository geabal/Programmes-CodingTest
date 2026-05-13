from collections import defaultdict
class FlightPlanner:
    def __init__(self, tickets):
        #edges: 가능한 모든 일방향 경로 기록. {출발지:[[도착지1, 티켓id1],[도착지2, 티켓id2]]...}
        self.edges = defaultdict(list)
        #isused: 해당 티켓을 사용했는지 여부 확인. 사용했다면 True, 사용하지 않았다면 False.
        self.isused={}
        #way: 경로 stack
        self.way = []
        #is_found_way: 정답을 찾았는지 여부
        self.is_found_way = False
        
        #edges, isused 초기화
        t_id = 0
        for start, end in tickets:
            t_id += 1
            if start in self.edges:
                self.edges[start].append([end, t_id])
            else:
                self.edges[start] = [[end,t_id]]
            self.isused[t_id] = False
            
        #edges 도착지 알파벳순으로 정렬. 알파벳 순 빠른 것을 우선 선택하도록 함.
        for start in self.edges.keys():
            self.edges[start] = sorted(self.edges[start], key= lambda x:x[0])
        return
    
    def getWay(self):
        #way에는 방문 공항, 해당 공항을 방문하기 위해 사용한 티켓번호가 들어간다.
        self.way = [['ICN',0]]
        start = 'ICN'
        # dfs 호출
        self.dfs(start)
        # way를 정답 출력 방식에 맞춰 변경
        ans = [end for end, t_id in self.way]
        return ans
    
    def dfs(self, start:str):
        # 이동가능한 목적지 정보 얻기
        dests_cand = self.edges[start]
        dests = [[end, t_id] for end, t_id in dests_cand if self.isused[t_id]==False]
        if start == "TIA":
            print(dests)
        if dests:        
            for dest in dests:
                if self.is_found_way:   #정답 경로를 찾았다면 더이상 순회하지 않고 빠져나옴.
                    break
                self.way.append(dest)
                self.isused[dest[1]] = True
                self.dfs(dest[0])
                if self.is_found_way == False:  #들어갔던 길이 잘못된 길인 경우
                    self.way.pop()
                    self.isused[dest[1]] = False
                    
        else:
            if self.is_allused():   #모든 티켓을 사용한 경우, 경로를 찾았다고 표시
                self.is_found_way = True
                return       
            # else:
            #     #잘못된 경로로 들어와 티켓을 모두 사용하지 못하고 막힌 경우
            #     #직전 경로 방문 여부를 취소하고 return
            #     end, t_id = self.way.pop()
            #     self.isused[t_id] = False
            #     return
        return
    
    def is_allused(self):
        #티켓을 전부 사용했는지 확인
        # 티켓의 개수 +1 만큼 공항을 방문하면 성공
        if len(self.way) == len(self.isused.keys()) + 1:
            return True
        else:
            False
        # for k, v in self.isused.items():
        #     #하나라도 티켓을 사용하지 않은 경우 False 반환
        #     if v == False:
        #         return False
        # return True

def solution(tickets):
    fp = FlightPlanner(tickets)
    answer = fp.getWay()
    return answer

