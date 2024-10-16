array = [
    46, 82, 21, 58, 22, 54, 71, 215, 99, 227, 
    73, 24, 17, 44, 244, 78, 25, 66, 47, 3, 
    87, 33, 312, 242, 42, 61, 348, 346, 98, 92, 
    83, 100, 94, 40, 5, 458, 364, 26, 64, 635, 
    90, 489, 72, 504, 88, 97, 226, 218, 186, 268
]

count = len(array)

def heapify(root, size):
    left_child = root*2 +1  #왼쪽 자식의 인덱스 공식 : root*2 +1
    if left_child >= size : return
    child = left_child
    right_child = root*2 +2 #오른쪽 자식: 루트 x2 +2
    if right_child < size:
        if array[left_child] > array[right_child]:
            child = left_child
    if array[root] < array [child]:
        array[root], array[child] = array[child], array[root]
        heapify(child, size)

def heap_sort(arr):
    pass

def main():
       print(f'before: {array}')
       heap_sort(array)
       print(f'after: {array}')

if __name__ == '__main__':
       main()