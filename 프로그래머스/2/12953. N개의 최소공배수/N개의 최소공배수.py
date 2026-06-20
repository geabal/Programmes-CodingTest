
# 두 수의 최소공배수를 구하는 메소드
def getlcm(a,b):
    for i in range(max(a,b), (a*b)+1):
        if i % a == 0 and i%b == 0:
            return i

def solution(arr):
    ans = arr[0]
    for i in range(len(arr)-1):
        next_num = arr[i+1]
        ans = getlcm(ans,next_num)

    return ans