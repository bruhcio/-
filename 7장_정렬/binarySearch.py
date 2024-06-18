import random
from selectionSort import selectionSort #insertionsort도 가능

def rBinarySearch(A, key, low, high):
    #low, high가 파라미터로 들어가야 재귀호출 가능
    if (low > high):
        return -1
    mid = (low + high) // 2
    print(A[mid], end=' ')

    if key == A[mid]:
        return mid
    elif key < A[mid]: # 미드 값이 중간값보다 아래에 있을 떄
        return rBinarySearch(A, key, low, mid -1)
    else:              # 미드 값이 중간값보다 위에 있을 때
        return rBinarySearch(A, key, mid + 1, high)

def iBinarySearch(A, key): ##애는 뭘까??
    low = 0
    high = len(A)

    while (low <= high):
        mid = (low + high) // 2
        print(A[mid], end=' ')

        if key == A[mid]:
            return mid
        elif key < A[mid]:
            high = mid - 1
        else:
            low = mid + 1
if __name__ == '__main__':
    A = []
    for i in range(15):
        A.append(random.randint(1,100))

    selectionSort(A)
    print('A[] = ', A)

    key = int(input('Input search key : '))
    print('rbinary search : %d' %rBinarySearch(A, key, 0, 14))