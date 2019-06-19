def linear_search(A, key):
    flag = False
    position = 0

    while position < len(A) and not flag:
        if A[position] == key:
            flag = True
        else:
            position += 1
    return flag


A = [84, 21, 47, 96, 15]
found = linear_search(A, 15)

print(["Not Found", "Found"][found])