import bisect

def insertionSort(arr):
    for i in range(len(arr)):
        e = arr[i]
        ind = bisect.bisect_left(arr[:i], e)
        if ind != i:
            arr.insert(ind, e)
            arr.pop(i+1)
    return arr

def insertionSort2(arr):
    for i in range(1, len(arr)):
        value = arr[i]
        pos = i

        while pos > 0 and arr[pos-1] > value:
            arr[pos] = arr[pos-1]
            pos-=1

        arr[pos] = value
    return arr

arr = [14,3,6,7,9,1,5]

print(insertionSort(arr))
print(insertionSort2(arr))