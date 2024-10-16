array = [
    46, 82, 21, 58, 22, 54, 71, 215, 99, 227, 
    73, 24, 17, 44, 244, 78, 25, 66, 47, 3, 
    87, 33, 312, 242, 42, 61, 348, 346, 98, 92, 
    83, 100, 94, 40, 5, 458, 364, 26, 64, 635, 
    90, 489, 72, 504, 88, 97, 226, 218, 186, 268
]



GAPS = [1750, 701, 301, 141, 63, 31, 15, 7, 3, 1, 0]

def next_gap(gap):
  for g in GAPS: 
    if gap > g: return g



def shell_sort(arr):
    count = len(array)
    gap = next_gap(count/2.5)
    while gap >0:
        for offset in range(gap):
            start = offset + gap
            while start < count:
                min_value = arr[start]
                i = start
                while i >=gap:
                    if arr[i -gap] > min_value:
                        arr[i] = arr[i-gap]
                        i -= gap
                    else:
                        break
                arr[i] = min_value
                start += gap
        gap = next_gap(gap)


def main():
       print(f'before: {array}')
       shell_sort(array)
       print(f'after: {array}')

if __name__ == '__main__':
       main()