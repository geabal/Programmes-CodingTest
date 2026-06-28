from collections import defaultdict
from math import ceil


def getfee(park_time, fees):
    basic_time, basic_fee, plus_time, plus_fee = fees
    if park_time > basic_time:
        result = basic_fee + ceil((park_time-basic_time)/plus_time)*plus_fee
    else:
        result = basic_fee
    return result
    
def getpt(it, ot):
    # 주차 시간 계산. 출차 시간 - 입차 시간을 분으로 반환
    in_time = list(map(int, it.split(':')))
    out_time = list(map(int, ot.split(':')))
    
    if out_time[1] < in_time[1]:
        out_time[1] += 60
        out_time[0] -= 1
    
    res = (out_time[1] - in_time[1]) + 60*(out_time[0] - in_time[0])
    
    return res

def solution(fees, records):
    answer = []
    # 차량 번호 별 [입차, 출차 시간], 누적 주차 시간 기록
    times = defaultdict(dict)
    for record in records:
        #t: 기록 시간, car: 차 번호, act: 출차인지 입차인지
        t, car, act = record.split()
        if act == 'IN':
            if 'time_stack' in times[car]:
                times[car]['time_stack'].append(t)
            else:
                times[car]['time_stack'] = [t]
                
        elif act =='OUT':
            in_time = times[car]['time_stack'].pop()
            park_time = getpt(it=in_time, ot=t)
            #주차 시간 누적으로 기록
            if 'park_time' in times[car]:
                times[car]['park_time'] += park_time
            else:
                times[car]['park_time'] = park_time
        
    #입차만 하고 출차하지 않은 주차시간 계산
    for k,v in times.items():
        if ('time_stack' in v) and len(v['time_stack'])>0:
            out_time = '23:59'
            in_time = times[k]['time_stack'].pop()
            park_time = getpt(it=in_time, ot=out_time)
            if 'park_time' in times[k]:
                times[k]['park_time'] += park_time
            else:
                times[k]['park_time'] = park_time
        
    
    #요금 계산
    for k,v in times.items():
        park_fee = getfee(times[k]['park_time'], fees)
        times[k]['park_fee'] = park_fee
    
    #차량번호가 작은 자동차부터 출력하기 위해 오름차순 정렬.
    sorted_times = sorted(times.items(), key=lambda x:x[0])
    print(sorted_times)
    answer = [v['park_fee'] for k, v in sorted_times]
    return answer