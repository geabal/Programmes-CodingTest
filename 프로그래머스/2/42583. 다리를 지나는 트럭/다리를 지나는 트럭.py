from collections import deque

def solution(bridge_length, weight, truck_weights):

    trucks_deque = deque(truck_weights)
    
    #경과한 시간 체크
    time_checker = 0
    # bridge: 현재 다리 위에 있는 트럭들. 각 요소는 [트럭 무게, 다리를 건넌 시간]으로 기록.
    bridge = deque()
    # weight_now: 현재 다리 위에 올라간 트럭 무게
    weight_now = 0
    
    # 대기 트럭과 다리를 건너는 트럭이 모두 없어질 때까지 순회
    while trucks_deque or bridge:
        time_checker += 1
        #다리 위에 있는 모든 트럭의 다리를 건넌 시간 +1
        for i in range(len(bridge)):
            bridge[i][1] += 1
        
        #가장 앞에 있는 트럭이 다리 끝에 도달한 경우, pop left
        #트럭은 한번에 한대만 지나가므로 가장 앞의 트럭만 도달 여부 체크
        if bridge and bridge[0][1] ==bridge_length:
            gone_truck = bridge.popleft()
            # 다리를 지나간 트럭만큼 현재 무게 빼기
            weight_now -= gone_truck[0]
        
        #다리에 추가로 트럭을 올릴 수 있는지 확인
        #대기 트럭이 없는 경우 continue
        if not trucks_deque:
            continue
        if weight_now+trucks_deque[0] <= weight:
            new_truck = trucks_deque.popleft()
            bridge.append([new_truck, 0])
            weight_now += new_truck
        
    
    return time_checker