#선택문제: n개의 숫자들 중에서 k번째로 작은 숫자를 찾는 문제

import random

words = [
    '2023180009', 'hut', 'apostle', 'equipment', 'fop', 'refined', 'parapet', 'mog', 'amputate', 'covetous', 'somebody', 
    'all', 'lobbyist', 'remark', 'subscriber', 'quorum', 'steppe', 'clean', 'cu', 'commend', 'prosy',
    'supererogation', 'indignation', 'wolverine', 'emporium', 'intersect', 'constitution', 'miscast', 'rabbi', 'enmity', 'loft',
    'temporize', 'speedboat', 'agenda', 'delusion', 'class01', 'idolize', 'romance', 'overestimate', 'revive', 'smell', 
    'toast', 'singe', 'inlay', 'field', 'speed', 'farad', 'adult', 'pansy', 'crawl', 'smith', 'exude', 
    'froze', 'litho', 'inuit', 'fakir', 'noddy', 'sheen', 'sandy', 'gaffe', 'spark', 'cavil', 'tenor', 
    'clonk', 'stung', 'boult', 'inapt', 'taker', 'cliff', 'shine', 'sable', 'agile', 'evens', 'pluck', 
    'blade', 'niece', 'paste', 'theft', 'young', 'bonny', 'aggro', 'bevel', 'rebel', 'clown', 'quote', 
    'horsy', 'wrong', 'hindu', 'acute', 'sloop', 'tuner', 'expel', 'motel', 'divan', 'gesso', 'strop', 
    'lance', 'lifer', 'dunce', 'lemur', 'scree', 'basic', 'wring', 'graph', 'conch', 'favor', 'anise', 
    'value', 'queue', 'poppy', 'staid', 'snook', 'spurt', 'canto', 'sprat', 'first', 'sidle', 'douse', 
]

def selection(arr, start, end, nth):
		# pi = qs.partition(arr, start, end)		#pivot 인덱스
	# ss = pi - start #smalgroup의 size
	# #smalgroup의 size 와 몇번째(nth)을 찾을거냐 --> case 3개
	# ss vs nth
	# case ss == nth-1:
	# 	return arr[pi]
	# case <
	# 	return selection(start ~ pi-1)
	# case >
	# 	return selection(pi+1 ~ end)

	pass

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

	
def main():
	print(f'{words}')

	# ranks = [3, 17, 23, 88, 99 ]

	# last_word_index = len(qs.words ) -1
	# for rank in ranks:
	# 	words = qs.words[:]
	# 	word = selection(words, 0, last_word_index, rank)
	# 	word = words[rank-1]		
	# 	print(f'{rank=} {word =}')

if __name__ == '__main__':
	main()