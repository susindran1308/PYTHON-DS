
# def quicksort(arr, low, high):
#     if low < high:
#         pivot = high
#         j=low
#         i=low-1

#         for j in range(low, high):
#             if arr[j] <= arr[pivot]:
#                 i+=1
#                 arr[j], arr[i] = arr[i], arr[j]
#         pivot = i+1

#         quicksort(arr, low, pivot-1)
#         quicksort(arr, pivot+1, high)



def quicksort(arr, low, high):
    if low<high:
        p = partition(arr, low, high)
        quicksort(arr, low, p-1)
        quicksort(arr, p+1, high)

def partition(arr, low, high):
    i = low-1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]

    return i+1

arr = [4,6,2,8,9,3,7]
quicksort(arr, 0, len(arr)-1)

print(arr)