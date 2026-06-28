from math import sqrt

def n2k(n, k):
    ''' 숫자 n을 k 진수 소수(str)로 변환 '''
    tmp = n
    knum = ''
    while tmp > 0:
        tmp, mod = divmod(tmp,k)
        knum += str(mod)
    
    return knum[::-1]

def isprime(num):
    if num == 1 or num == 0:
        return False
    if num ==2:
        return True
    
    max_p = int(sqrt(num)) +1
    for i in range(2,max_p):
        if num%i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    knum_str = n2k(n,k)
    knums = knum_str.split('0')
    
    for knum in knums:
        #10진수 변환
        if not knum:
            continue
        ten_n = int(knum)
        #10진수 변환된 수가 소수인지 확인
        if isprime(ten_n):
            answer+= 1
    
    return answer