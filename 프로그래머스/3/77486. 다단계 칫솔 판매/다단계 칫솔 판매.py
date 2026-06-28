def solution(enroll, referral, seller, amount):
    # enroll: 전체 사람 명단
    # referral: 해당 노드의 부모 노드. "-"는 센터노드를 부모로 둔다는 뜻.
    # seller[n]:aount[n] : n번째 사람이 판매한 상품 수. 각 상품은 100원
    answer = {'-':0}    # center에 대한 이익값도 기록
    for name in enroll: # 이익값 0으로 초기화
        answer[name] = 0
    
    par = {'-':'-'}    # 각 자식 노드의 부모 노드 기록.
    for i, er in enumerate(enroll):
        par[er] = referral[i]
        
    for s, a in zip(seller, amount):
        # 각 판매건에 대해 얻는 이득 계산
        now_node = s
        now_cash = 100 * a
        answer[now_node] += now_cash
        par_node = par[now_node]
        while now_node != '-' and now_cash>0:  #현재 노드가 '-'가 되면 멈춘다.
            par_cash = now_cash // 10
            answer[par_node] += par_cash
            answer[now_node] -= par_cash
            
            now_node = par_node
            par_node = par[now_node]
            now_cash = par_cash
        
    res = []
    for name in enroll:
        res.append(answer[name])
    return res