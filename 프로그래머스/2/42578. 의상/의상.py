from typing import Dict

def cal_set(closet:Dict):
    set_num = 1
    for cat, cloth_list in closet.items():
        # 각 종류별로 가지고 있는 옷의 가지 수 + 착용하지 않는 경우(1) 곱하기
        set_num *= (len(cloth_list) + 1)
    
    # 아무것도 착용하지 않는 경우 1개 제외
    set_num -= 1
    return set_num

def solution(clothes):
    # closet: 의상을 종류별로 정리한 dict
    closet = {}
    #cat: category. 의상 종류
    #cloth: 의상 이름
    for cloth, cat in clothes:
        if cat in closet:
            closet[cat].append(cloth)
        else:
            closet[cat] = [cloth]
    
    # 경우의 수 계산
    answer = cal_set(closet)

    return answer