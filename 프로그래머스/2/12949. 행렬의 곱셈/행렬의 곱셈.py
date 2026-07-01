def getcol(arr, n):
    res = []
    # 행렬의 n번째 열 값 list 리턴
    for i in range(len(arr)):
        res.append(arr[i][n])
    return res

def mtp_list(l1, l2):
    # 각 리스트의 자리값을 더한 총합 반환
    res = 0
    for a, b in zip(l1,l2):
        res += (a*b)
    return res

def solution(arr1, arr2):    
    # a1xa2 * b1xb2 = a1 x b2
    #행렬곱에서 결과 행렬의 크기는 첫 행의 행 x 두번째 행의 열
    rowl, coll = len(arr1), len(arr2[0])
    
    answer = [[0]*coll for _ in range(rowl)]
    
    #각 행렬에 들어갈 요소 계산
    for coli in range(coll):
        for rowi in range(rowl):
            row = arr1[rowi]
            col = getcol(arr2, coli)
            answer[rowi][coli] = mtp_list(row, col)
            
    
    return answer