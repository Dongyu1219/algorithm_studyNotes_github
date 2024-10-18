array = [
    46, 82, 21, 58, 22, 54, 71, 215, 99, 227, 
    73, 24, 17, 44, 244, 78, 25, 66, 47, 3, 
    87, 33, 312, 242, 42, 61, 348, 346, 98, 92, 
    83, 100, 94, 40, 5, 458, 364, 26, 64, 635, 
    90, 489, 72, 504, 88, 97, 226, 218, 186, 268
]

def heapify(root, size):
    left_child = root*2 +1  #왼쪽 자식의 인덱스 공식 : root*2 +1
    if left_child >= size : return  #힙구조 끝
    child = left_child
    right_child = root*2 +2 #오른쪽 자식: 루트 x2 +2
    if right_child < size:  # lc 만 있을 수도 있지만, rc 도 있다면
        if array[right_child] > array[left_child]: #큰 것을 비교하여
            child = right_child                     #child에 담는다
    if array[root] < array [child]: # parent 와 child 중에 어느것이 큰지 비교하여               
        array[root], array[child] = array[child], array[root] #더 크면 교체
        heapify(child, size) # 교체되어 내려간 child 를 새로운 parent 로 하여 재귀 호출한다

def heap_sort(arr):
    pass

def main():
    count = len(array)
    last_parent_index = count //2-1 #:가장 마지막에 부모 인덱스를 구하는 공식
    # 이유 : 완전 이진 트리 특성상 자식이 있는 노드는 반 드 시 절반이다.
    n = last_parent_index
    print(f'before: {array}')
    for n in range(last_parent_index, -1, -1):
        heapify(n, count)

    last_sort_index = count -1 
    while last_sort_index>0:
        array[0], array[last_sort_index] = array[last_sort_index], array[0]
        heapify(0, last_sort_index)
        last_sort_index -=1
    
    print(f'after: {array}')

if __name__ == '__main__':
       main()