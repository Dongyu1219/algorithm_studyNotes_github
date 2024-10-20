array = [
    46, 82, 21, 58, 22, 54, 71, 215, 99, 227, 
    73, 24, 17, 44, 244, 78, 25, 66, 47, 3, 
    87, 33, 312, 242, 42, 61, 348, 346, 98, 92, 
    83, 100, 94, 40, 5, 458, 364, 26, 64, 635, 
    90, 489, 72, 504, 88, 97, 226, 218, 186, 268
]

count = len(array)

def merge(left, right ,end):                     #왼쪽은 [left ~ right-1] 오른쪽은 [right~end]
       merged= []                                #임시 저장할 목록 준비
       l ,r = left, right                        #양쪽의 첫번째 선수 입장
       while l < right and r<= end:              #한쪽이라도 소진되면 stop
              if array [l] <= array [r]:         #두 팀에서 출전한 선수끼리 겨룬다.
                     merged.append(array[l])     #왼쪽 팀 선수가 졋을때 왼쪽 팀 선수를 목록에 추가하고 
                     l+=1                        #왼쪽 다음 선수 입장
              else :                             #아니면
                     merged.append(array[r])     #오른쪽 선수가 졋을때 : 오른족 선수 목록에 append 하고 
                     r+=1                        #다음 오른쪽 선수 입
                                                 #while문 끝남 : 왼쪽 선수 소진이거나 오른쪽 선수 소진
       while l< right:                           #왼쪽 선수가 남아 있을때
              merged.append(array[l])            #왼쪽 선수 모두를 리스트에 추가
              l+=1
       while r<= end:                            #오른쪽 선수 남아 있을때
              merged.append(array[r])            #오른쪽 선수를 모두 리스트에 추가
              r+=1
       #아래 과정을 slicing으로 간결하게 처리
       array[left:end+1] = merged
       #l = left                                  # left: merge 시작 값
       #for n in merged:                          # 임시 저장되어 있던 결과 목록에 있는 선수들을
              #array[l] = n                       # 원래의 배열에 옮겨 담는다
              #l += 1

#하나의 배열을 정렬하기 위해서는 둘로 나누어 왼쪽을 정렬하고 오른쪽을 정렬한뒤 두 배열을 합병하는 것이다.
def merge_sort(left, right):                     # right 포함
       if right <= left : return                 #정렬한 선수들이 없거나(<), 한명뿐이면(=) 정렬할 필요가 없다.
       #===============================================
       #성능 개선 1:
       #남은 원소가 2개뿐이면 직접 비교한다. 
       #if right == left+1:
       #       if array[left] > array[right]:
       #              array[left], array[right] = array[right], array[left]
       #      return
       #성능 개선2:
       #정렬할 배열의 크기가 8개 이하일때는 삽입 정렬로 진행한다.
       if right < left+8:
              insertion_sort(left, right)
              return
       #=================================================
       mid = (left+ right) //2                   #목록을 절반으로 나눈다.
       merge_sort(left, mid)                     #왼쪽 팀을 정렬한다. [왼쪽 sort] 
       merge_sort(mid+1, right)                  #오른쪽 팀을 정렬한다. [오른쪽 sort]
       merge(left, mid+1 ,right)                 #합병 [merge]
       pass
#정렬할 배열의 크기가 8개 이하일때는 삽입 정렬로 진행한다.
def insertion_sort(left, right):
       for i in range(left+1, right+1):
              v= array[i]
              j = i-1
              while j>=left and array[j] >v:
                     array[j+1] = array[j]
                     j-=1
              array[j+1] = v

              
def main():
       print(f'before: {array}')
       merge_sort(0, count-1)                    #전체 팀을 정렬한다.
       print(f'after: {array}')

if __name__ == '__main__':
       main()