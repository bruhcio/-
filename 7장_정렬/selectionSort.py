def printStep(l, idx): #fltmxmdhk guswo rlwnsdnlcl
    print(' step %d : ' %idx, end='')
    print(l)

def selectionSort(l):
    n = len(l)
    for i in range(n-1):
        least = i
        for  j in range(i+1, n):
            if l[j] < l[least]:
                least = j

            l[i], l[least] = l[least], l[i]
        printStep(l, i+1)


def insertionSort(L):
    n = len(L)

    for i in range(1, n):
        key = L[i]
        j = i - 1
        while j >= 0 and L[j] > key:
            L[j + 1] = L[j]
            j -= 1
            L[j + 1] = key
        printStep(L, i)


if __name__ == '__main__':
    data = [5,3,8,4,9,1,6,2,7]
    l = list(data)
    print("Before : ", l)
    selectionSort(l)
    print("selection : ", l)
    print()

    l = list(data)
    print("Before : ", l)
    insertionSort(l)
    print("insertion : ", l)
    print()

    # 선택 정렬 알고리즘은 안정성을 보장하지 않는다.
