def binary_search(A, key):
    low = 0
    high = len(A) - 1
    flag = False

    while low <= high:

        mid = (low+high)//2

        if A[mid] < key:
            low = mid+1
        elif A[mid] > key:
            high = mid-1
        elif A[mid] == key:
            flag = True
            break
    return flag

A = [12, 23, 34, 45, 56, 67]
key = 23

found = binary_search(A, key)

print(["Not Found", "Found"][found])