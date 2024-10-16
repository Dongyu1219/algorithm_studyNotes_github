array = [
    46, 82, 21, 58, 22, 54, 71, 215, 99, 227, 
    73, 24, 17, 44, 244, 78, 25, 66, 47, 3, 
    87, 33, 312, 242, 42, 61, 348, 346, 98, 92, 
    83, 100, 94, 40, 5, 458, 364, 26, 64, 635, 
    90, 489, 72, 504, 88, 97, 226, 218, 186, 268
]

count = len(array)

def selection_sort(arr):
       for i in range(count):
              min_value = arr[i]  
              min_at= i
              for j in range (i+1, count):
                     if arr[i] > arr[j]:
                            min_value = arr[j]
                            min_at = j
                            arr[i], arr[j] = arr[j], arr[i]

def main():
       print(f'before: {array}')
       selection_sort(array)
       print(f'after: {array}')

if __name__ == '__main__':
       main()