def solution(routes):
    # 1. 진입 지점 기준 오름차순 정렬
    routes = sorted(routes, key=lambda x:x[1])
    
    # 2. 첫 나간 지점 > 다음 진입 지점 여부 확인
    camera_num = 1
    start_out = routes[0][1]
    for r in routes:
        now_in = r[0]
        if now_in <= start_out:
            continue
        else:
            camera_num += 1
            start_out = r[1]
        

    return camera_num