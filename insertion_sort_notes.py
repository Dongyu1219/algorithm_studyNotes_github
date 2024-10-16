array = [
    46, 82, 21, 58, 22, 54, 71, 215, 99, 227, 
    73, 24, 17, 44, 244, 78, 25, 66, 47, 3, 
    87, 33, 312, 242, 42, 61, 348, 346, 98, 92, 
    83, 100, 94, 40, 5, 458, 364, 26, 64, 635, 
    90, 489, 72, 504, 88, 97, 226, 218, 186, 268
]

count = len(array)

def insertion_sort(arr):
    for i in range(1, count):           #첫번째 [0] 은 정렬되어 있다! 1부터
        for j in range(i,0, -1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else:
                break;

def insertion_sort2(arr):   #개선
        for i in range(1, count):
            value = arr[i]
            j = i
            while j > 0:
                if arr[j-1] > value:
                    arr[j], arr[j-1] = arr[j-1], arr[j]
                    j-=1
                    arr[j] = value
                else:
                    break

def main():
       print(f'before: {array}')
       insertion_sort2(array)
       print(f'after: {array}')

if __name__ == '__main__':
       main()