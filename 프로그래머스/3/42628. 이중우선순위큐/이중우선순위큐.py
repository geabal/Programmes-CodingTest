from heapq import heappop, heappush

#이중우선순위 큐 클래스 구현
class MinMaxHeap:
    id_now = 0
    def __init__(self):
        #최소힙
        self.minh = []
        #최대힙
        self.maxh = []
        #해당 id의 데이터가 존재하는지 확인하는 dict. {id:bool}
        self.data_idx={}
        return
    
    def minpop(self):
        data = [0,0]
        while len(self.minh)>0:
            data = heappop(self.minh)
            #이미 pop했던 데이터인지 확인
            if self.data_idx[data[1]]==True:  #현재 존재하는 데이터인 경우
                self.data_idx[data[1]] = False
                break
            else:   # 현재 존재하지 않은 데이터를 뽑은 경우,
                if len(self.minh)==0:
                    return 0
                continue    # 존재하는 데이터를 pop 할 때까지 while 순회
        return data[0]
    
    def maxpop(self):
        data = [0,0]
        while len(self.maxh)>0:
            data = heappop(self.maxh)
            #이미 pop했던 데이터인지 확인
            if self.data_idx[data[1]]==True:  #현재 존재하는 데이터인 경우
                self.data_idx[data[1]] = False
                break
            else:   # 현재 존재하지 않은 데이터를 뽑은 경우,
                if len(self.maxh)==0:
                    return 0
                continue    # 존재하는 데이터를 pop 할 때까지 while 순회
        return data[0] * (-1)
    
    def insert(self, num:int):
        # id 정보 추가
        self.id_now += 1
        data = (num, self.id_now)
        self.data_idx[self.id_now] = True
        # min heap 데이터 추가
        heappush(self.minh, data)
        # max heap 데이터 추가
        minus_data = (num *(-1), self.id_now)
        heappush(self.maxh, minus_data)
        
        return
    
    def isheap(self):
        
        if self.minh and self.maxh:
            return True
        else:
            return False
        
    def getMax(self):
        while True:
            k = self.maxh[0][1]
            if self.data_idx[k] == False:
                heappop(self.maxh)
                if len(self.maxh)==0:
                    return 0
            else:
                return self.maxh[0][0] * (-1)
    
    def getMin(self):
        while True:
            k = self.minh[0][1]
            if self.data_idx[k] == False:
                heappop(self.minh)
                if len(self.minh)==0:
                    return 0
            else:
                return self.minh[0][0]
        

def solution(operations):
    mmheap = MinMaxHeap()
    for operation in operations:
        ops = operation.split(' ')
        if ops[0] == 'I':   #insert를 하는 경우
            mmheap.insert(int(ops[1]))
        else:   #pop을 하는 경우
            if ops[1] == '-1':
                mmheap.minpop()
            elif ops[1] =='1':
                mmheap.maxpop()

    answer = [0,0]
    if mmheap.isheap():
        answer[0] = mmheap.getMax()
        answer[1] = mmheap.getMin()

    return answer