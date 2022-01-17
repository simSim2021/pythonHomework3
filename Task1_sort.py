
# сортировка shaker
def ShakerSort(A):
    for i in range(len(A) // 2):
        for j in range(len(A) - 1 - i):
            if A[j] > A[j + 1]:
                a = A[j]
                A[j] = A[j + 1]
                A[j + 1] = a
        for j in range(len(A) - 2 - i, i + 1, -1):
            if A[j] < A[j - 1]:
                a = A[j]
                A[j] = A[j - 1]
                A[j - 1] = a
    return A

# сортировка select


def selSort(A):
    for i in range(len(A) - 1):
        minIndex = i
        minVal = A[i]
        j = i + 1
        while j < len(A):
            if minVal > A[j]:
                minIndex = j
                minVal = A[j]
            j += 1
        temp = A[i]
        A[i] = A[minIndex]
        A[minIndex] = temp
    return A


print('ShakerSort')
print(ShakerSort([121, 15, 0, 3, 8, 25, 96, 3]))

print('SelectSort')
print(selSort([121, 15, 0, 3, 8, 25, 96, 3]))


