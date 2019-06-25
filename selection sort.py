def selectionsort(arr):
    l = len(arr)
    for i in range(l-1, 0 , -1):
        maxPosition = 0
        for j in range(1, i+1):
            if arr[j] > arr[maxPosition]:
                maxPosition = j
        arr[i], arr[maxPosition] = arr[maxPosition], arr[i]
    return arr

arr = [14,3,6,7,9,1,5]

print(selectionsort(arr))