def dfs(b, i, depth):
    if depth == 0:   #리프 노드에 도달한 경우, 포화이진트리
        return True
    # i: 부모노드의 위치
    # 부모노드가 더미인 경우, 왼쪽 or 오른쪽 자식이 1일때 이진트리 불가
    elif b[i] == '0':
        if b[i-depth] == '1' or b[i+depth] == '1' : return False
    
    #왼쪽 자식 서브트리 탐색
    left = dfs(b, i-depth, depth//2)
    right = dfs(b, i+depth, depth//2)
    return left and right

def isCBT(num:int):
    '''
    들어온 숫자가 완전이진트리로 표현가능한지 확인하는 함수.
    표현 가능하면 1, 아니면 0
    '''
    #바이너리 표현형으로 변환
    bin_num = str(bin(num))[2:]
    
    # 바이너리 표현형의 앞에 0을 붙여 2**(n)-1 자리수 표현형으로 만들어준다.
    # ex. 11 -> 011
    if len(bin_num) > 1:    # number가 1이라면 그냥 통과
        tmp = len(bin_num) + 1
        n = 0
        while tmp > 1:
            tmp /= 2
            n += 1
        if tmp // 1 != tmp: # 자리수가 2**(n)-1 개가 아닌 경우, 모자란만큼 앞에 0 붙임
            additional_zero = (2**n) -1 - len(bin_num)
            bin_num = ('0'*additional_zero) + bin_num
            

    # 이진트리 표현이 가능한지 체크
    # 부모가 더미인데 자식이 1인 경우가 있으면 표현 불가
    result = dfs(bin_num, len(bin_num)//2, (len(bin_num)+1)//4)
    if result:
        return 1
    else:
        return 0

def solution(numbers):
    answer = []
    for num in numbers:
        answer.append(isCBT(num))
    return answer