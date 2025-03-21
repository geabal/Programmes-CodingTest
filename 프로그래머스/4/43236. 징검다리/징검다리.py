def solution(distance, rocks, n):
    answer = 0
    
    rocks.append(distance)
    rocks = sorted(rocks)
    
    left, right = 0, distance
    
    while left <= right:
        mid = (left+right)//2
        min_dist = float('inf')
        cur = 0
        remove_cnt = 0
        
        for rock in rocks:
            diff = rock - cur
            if diff < mid:
                remove_cnt += 1
            else:
                cur = rock
                min_dist = min(min_dist, diff)
        if remove_cnt > n:
            right = mid - 1
        else:
            answer = min_dist
            left = mid + 1
    
    return answer