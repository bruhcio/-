N = 100 #size??

class MaxHeap:
    def __init__(self):
        self.heap = [None] * N
        self.heapSize = 0

    def insertItem(self, item): # 데이터를 추가하는 함수
        self.heapSize += 1
        self.heap[self.heapSize] = item
        self.upHeap()

    def upHeap(self):           # 데이터 값 비교 후에 추가한 데이터를 올리는 함수
        i = self.heapSize       # i == 11번 위치임
        item = self.heap[i]     # item == 데이터 8이 들어감

        while (i != 1) and (item > self.heap[i // 2]): # 내 위의 노드의 데이터 값을 위에서 밑으로 내린다.
            self.heap[i] = self.heap[i // 2]           # 현재 5번의 데이터 값을 내려와 있지만 아직 올리지는 않음
            i = i // 2                                 # i = 5, 값은 2가 됨

        self.heap[i] = item


    def removeitem(self):
        item = self.heap[1]                            # root node를 아이템에 저장시킴
        self.heap[1] = self.heap[self.heapSize]        # 루트 노드에 맨 마지막 노드의 데이터 값을 저장
        self.heapSize -= 1
        self.downHeap()

        return item

    def downHeap(self):
        item = self.heap[1]
        parent = 1                                      # root node 위치 번호
        child = 2                                       # 루트 노드의 왼쪽 노드

        while child <= self.heapSize:                   # while문에서도 조건 걸고, 같은 조건을 if문에서도 거는 이유 : 자식 노드가 1개일 경우 생각
            if (child < self.heapSize) and (self.heap[child + 1] > self.heap[child]):
                child += 1

            if item >= self.heap[child]:
                break

            self.heap[parent] = self.heap[child]
            parent = child
            child *= 2

        self.heap[parent] = item

if __name__ == "__main__":
    H = MaxHeap()
    data = [7, 3, 5, 6, 4, 9, 2, 3, 1, 2]

    for e in data:
        H.insertItem(e)
        print("Heap : ", H.heap[1:H.heapSize + 1])
    print()

    print(f"{H.removeitem()} is deleted")
    print("Heap : ", H.heap[1:H.heapSize + 1])

    print(f"{H.removeitem()} is deleted")
    print("Heap : ", H.heap[1:H.heapSize + 1])


#최대 힙이 있는데 데이터가 어쩌고 저쩌고 들어감
#결과 힙은 어떻게 됨??
# 딜리트 힙을 몇 번 했을 때 출력 값은??