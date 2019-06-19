
def binarysearch(A, key, low, high):
    mid = (low+high)//2

    if low > high:
        return False

    if key < A[mid]:
        return binarysearch(A, key, low, mid-1)

    elif key > A[mid]:
        return binarysearch(A, key, mid+1, high)

    elif key == A[mid]:
        return True

A = [12, 23, 34, 45, 56]

key = 23

found = binarysearch(A, key, 0, len(A)-1)

print(["Not Found", "Found"][found])