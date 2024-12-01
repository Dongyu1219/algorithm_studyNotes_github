edges=[
    (0, 2, 267), (0, 10, 292), (0, 14, 162), (0, 17, 311), (0, 23, 281), 
    (1, 11, 331), (1, 19, 307), (1, 22, 395), (2, 6, 256), (2, 10, 319), 
    (2, 14, 111), (2, 16, 316), (2, 18, 405), (2, 20, 451), (2, 21, 415), 
    (2, 24, 488), (3, 8, 249), (3, 12, 438), (3, 15, 84), (4, 7, 445), 
    (4, 10, 53), (4, 16, 320), (4, 17, 135), (4, 20, 229), (4, 24, 298), 
    (5, 9, 367), (5, 13, 483), (5, 15, 261), (5, 19, 358), (6, 7, 109), 
    (6, 12, 358), (6, 14, 319), (6, 16, 456), (6, 18, 153), (6, 21, 465), 
    (7, 12, 440), (7, 13, 465), (7, 14, 210), (7, 23, 236), (8, 9, 106), 
    (10, 16, 285), (11, 13, 371), (11, 19, 53), (12, 13, 243), (12, 18, 364), 
    (12, 21, 395), (12, 22, 442), (13, 21, 170), (14, 18, 451), (14, 23, 318),
    (16, 17, 287), (16, 23, 325), (17, 24, 392), (19, 22, 146), (20, 24, 76)
]
num_vertex = 25
#edges(0, 2, 267) 뜻 : 노드 0 과 2가 간선으로 연결되어 있는데 그 비용은 267이다.

global roots
roots = [x for x in range(num_vertex)]     

mst = []


def append(s, e, w):
    if s <= e :
        mst.append((s, e, w))
    else:
        mst.append((e, s, w))
    mst.sort(key=lambda e:e[0]*1000+e[1])  #노드번호가 작은 순서대로 정렬


#트리 생기지 않게 하기 위해 경로 압축 추가
def union(u, v):            # ---> u와 v의 root를 합치자
    uroot = getRoot(u)
    vroot = getRoot(v)
    if uroot > vroot:           # 적은 숫자 쪽으로 합치자
        uroot, vroot = vroot, uroot
    roots[vroot] = uroot
    

def getRoot(v):                 #루트가 얼마냐
    if v != roots[v]:
        roots[v] = getRoot(roots[v])        #경로 압축(재귀 호출)
    return roots[v]


def spanning():             #지금 mst의 결과가 spanning tree인지 확인하는 함수
    return len(mst) >= num_vertex - 1         # 간선의 개수 == 노드의 개수 -1


def onSameTree(u, v):   #같은 트리에 있는지 확인
    if getRoot(u) == getRoot(v):
        return True
    

edges.sort(key=lambda e: e[2])        


for s,e,w in edges:
    if spanning(): break                #그래프가 spanning이 되면 즉시 중단 
    if onSameTree(s, e): continue       #root가 같은 간선은 추가하지 않는다.
    union(s,e)
    append(s, e, w)

print(mst)
