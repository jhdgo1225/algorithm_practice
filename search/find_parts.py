def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if target == array[mid]:
        return mid
    elif target > array[mid]:
        return binary_search(array, target, mid+1, end)
    else:
        return binary_search(array, target, start, mid-1)

n = int(input())
data1 = list(map(int, input().split()))
data1.sort()

m = int(input())
data2 = list(map(int, input().split()))

for i in data2:
    result = binary_search(data1, i, 0, n-1)
    if result == None:
        print('No', end=" ")
    else:
        print("Yes", end=" ")