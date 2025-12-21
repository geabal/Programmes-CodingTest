from itertools import combinations
from typing import List

def str2bin(s:str):
    '''
    숫자로 이루어진 문자열을 이진수로 바꾸는 함수
    예: 012 -> 0b111, 23->0b0011
    '''
    res = 0
    for num in s:
        res += (2**int(num))
    
    return res

def is_minimal(answer:List[str], c_key:str):
    '''
    c_key가 최소성을 만족하는지 체크하는 함수
    '''
    if len(answer) == 0:
        return True
    
    bin_c_key = str2bin(c_key)
    for ans_key in answer:
        bin_ans_key = str2bin(ans_key)
        if bin(bin_ans_key | bin_c_key) == bin(bin_c_key):
            return False

    return True

def solution(relation):
    answer = []
    # 한 튜플의 길이가 컬럼의 개수
    cols = [i for i in range(len(relation[0]))]
    
    # 후보키는 최대 len(cols) 개의 컬럼으로 이루어질 수 있다.
    MAX_LEN_CANDIDATE_KEY = len(cols)
    NUM_ROWS = len(relation)
    
    # 후보키 리스트를 얻는 부분
    for len_candidate_key in range(1, MAX_LEN_CANDIDATE_KEY+1):
        # 후보키 그룹을 길이 len_candidate_key인 combination으로 선출
        candidate_group = combinations(cols, len_candidate_key)

        for c_key in candidate_group:
            # 해시맵으로 유일성 체크
            c_key_checker = set() 
            
            for row in relation:
                key = '_'.join([row[col] for col in c_key])
                c_key_checker.add(key)
            
            if len(c_key_checker) == NUM_ROWS:
                c_key_str = ''.join([str(col) for col in c_key])
                if is_minimal(answer, c_key_str):
                    answer.append(c_key_str)
        
    print(answer)
    return len(answer)