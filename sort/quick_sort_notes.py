array = [
    46, 82, 21, 58, 22, 54, 71, 215, 99, 227, 
    73, 24, 17, 44, 244, 78, 25, 66, 47, 3, 
    87, 33, 312, 242, 42, 61, 348, 346, 98, 92, 
    83, 100, 94, 40, 5, 458, 364, 26, 64, 635, 
    90, 489, 72, 504, 88, 97, 226, 218, 186, 268, 1
]

count = len(array)

def partition(left, right):
       pi = left                          #가장 왼쪽 값을 피벗으로 삼는다. pi = pivot index
       pivot = array[pi]                  #pivot = value

       p, q = left, right +1              #후보 선수들 출전 준비

       while True:                        # p와 q 가 역전할 때 까지
              while True:                 #왼쪽에서 pivot보다 큰 값을 찾을 때 까지
                     p += 1

                     if p > q: break
                     if p >right or array[p] >= pivot: break
                     #왼쪽에서 피벗보다 큰 값을 찾았다

              while True:                 #오른쪽에서 pivot보다 작은 값을 찾을 때 까지
                     q-=1
                     if q < p: break
                     if q<left or array[q] <= pivot: break
                     #오른쪽에서 pivot보다 작은 값을 찾았다.
                 
              if p >= q: break            #p와 q 가 만날때까지 계속 진행한다.
              array[p], array[q] = array[q], array[p]
              #array[p]와 array[q]를 교체한다. p이하에는 pivot보다 작은 값만, 
              #q이상에서는 pivot보다 큰 값만 있다
              
       #pivot의 위치를 확정시킨다.
       #pivot 값은 왼쪽 그룹 중에서 가장 큰 값이므로 q 위치로 옮긴다.
       #left가 q와 같다면 pivot보다 작은 것이 하나도 없다는 뜻이므로 옮길 필요가 없다.
       if left !=q:
              array[left], array[q]= array[q], array[left]
       return q                           #q위치를 리턴


def quick_sort(left, right):     
       if left >= right: return           #정렬할 것이 없으면 확정
       pivot = partition(left, right)     #피벗 위치 결정: partition 함수( pivot = partition(0, count-1) )
       quick_sort(left, pivot-1)          #pivot 보다 왼쪽 그룹을 다시 퀵소트
       quick_sort(pivot+1, right)         #pivot 보다 오른쪽 그룹을 다시 퀵소트

def main():
       print(f'before: {array}')
       quick_sort(0, count-1)
       print(f'after: {array}')

if __name__ == '__main__':
       main()