from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

class RouteGame:
    preorder_list = []
    postorder_list = []
    
    def __init__(self, nodeinfo):
        # info를 y 내림차순, x오름차순 정렬
        self.nodeinfo = nodeinfo
        for i in range(len(self.nodeinfo)): #self.nodeinfo = list([x, y, 노드 번호])
            nodeinfo[i].append(i+1)
        #y 내림차순, x 오름차순 정렬
        self.nodeinfo = sorted(self.nodeinfo, key=lambda x:(-x[1], x[0]))
        self.makeTree()
        return
    
    def makeTree(self):
        # 트리를 구하는 메소드
        #levels: 각 레벨에 어떤 x값이 있는지 기록
        levels = defaultdict(list)
        for x, y, node in self.nodeinfo:
            levels[y].append([x, node])
        
        # tree: {부모 node: {left: node, right: node}}
        self.tree = defaultdict(dict)
        MAX_LEVEL = self.nodeinfo[0][1]
        # levels[level] = list([x, node, x 최소값, x 최대값])
        levels[MAX_LEVEL][0].extend([-1, 100001])
        par_nodes = levels[MAX_LEVEL]
        for lv in range(MAX_LEVEL-1, -1, -1):
            children = levels[lv]
            if not children:    # y좌표에 노드가 없는 경우 pass
                continue
            par_i = 0
            par_x, par_node, low, high = par_nodes[par_i]
            for i, child in enumerate(children):
                x, node = child
                if high < x:
                    #이진탐색으로 low < x < high인 par_i 찾기
                    par_i = self.get_par_i(x, par_nodes, par_i)
                    par_x, par_node, low, high = par_nodes[par_i]
                # while high < x:
                #     par_i += 1
                #     par_x, par_node, low, high = par_nodes[par_i]
                    
                if low < x and x < par_x:
                    self.tree[par_node]['left'] = node
                    #최소, 최대 범위 제약조건 추가
                    levels[lv][i].extend([low,par_x])
                elif par_x < x and x < high:
                    self.tree[par_node]['right'] = node
                    levels[lv][i].extend([par_x,high])
            
            par_nodes = levels[lv]
        return
    
    def get_par_i(self, x, par_nodes, par_i_now):
        #이진탐색으로 low< x < high인 par_i 찾기
        l = par_i_now + 1
        r = len(par_nodes)-1
        m = (l+r)//2

        while l<=r:
            if len(par_nodes[m]) < 4:
                break
            par_x, par_node, low, high = par_nodes[m]
            if x < low:
                r = m-1
                m = (l+r)//2
            elif high < x:
                l = m+1
                m = (l+r)//2
            elif low < x and x < high:
                return m
            
        return m
    
    def preorder(self, root:int):
        left, right = 0, 0
        
        self.preorder_list.append(root)
        
        if 'left' in self.tree[root]:
            left = self.tree[root]['left']
            self.preorder(left)
        
        if 'right' in self.tree[root]:
            right = self.tree[root]['right']
            self.preorder(right)
        return
    
    def postorder(self, root:int):
        left, right = 0, 0
        
        if 'left' in self.tree[root]:
            left = self.tree[root]['left']
            self.postorder(left)
        
        if 'right' in self.tree[root]:
            right = self.tree[root]['right']
            self.postorder(right)
            
        self.postorder_list.append(root)
        
        return
        
    def get_root(self):
        return self.nodeinfo[0][2]
    
def solution(nodeinfo):
    rg = RouteGame(nodeinfo)
    root = rg.get_root()
    rg.preorder(root)
    rg.postorder(root)
    answer = [rg.preorder_list, rg.postorder_list]
    return answer