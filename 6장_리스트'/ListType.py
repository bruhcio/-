from ListNode import ListNode

#사이즈는 노드의 몇 개인지 말하는 거임
class ListType:
    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.head == None


    def insertFirst(self, data):
        node = ListNode(data, self.head)
        self.head = node
        self.size += 1

    def getNode(self, pos):
        p = self.head

        for i in range(1, pos -1):
            p = p.next

        return p #포지션 위치 이전 노드

    def insert(self, pos, data):
        if pos == 1:
            self.insertFirst(data)
        else:
            if(pos <= self.size + 1):
                p = self.getNode(pos)

                node = ListNode(data, p.next)
                p.next = node
                self.size += 1

            else:
                print('Invalid Pos')
    def display(self):
        p = self.head
        while(p!=None):
            print('[%s] -> ' %p.data, end = '')
            p = p.next
        print('\b\b\b   ')

    def deleteFirst(self):
        if self.isEmpty():
            print("List is Empty")
            return
        self.head = self.head.next
        self.size -= 1
    # def deleteFirst(self):
    #     if self.isEmpty():
    #         print("No element")
    #     else:
    #         p = self.head
    #         self.head = p.next
    #         self.size -= 1
    # 교수님 답안

    def delete(self, pos):
        if pos > self.size:
            print("Invalid position")
            return
        if pos == 1:
            self.deleteFirst()
        else:
            previous_node = self.getNode(pos - 1)
            if previous_node.next == None:
                print("삭제할 것이 없음", pos)
                return
        previous_node.next = previous_node.next.next
        self.size -= 1
    # def delete(self, pos):
    #     if self.isEmpty():
    #         print('no element')
    #         return
    #     if pos == 1:
    #         return self.deleteFirst()
    #     else:
    #         if pos <= self.size:
    #             q = self.getNode(pos)
    #             p = self.getNode(pos+1) #실제 삭제될 애
    #             q.next = p.next
    #             self.size -= 1
    #             return p.data
    #             교수님 답안
if __name__ == "__main__":
    L = ListType()

    L.insertFirst('A')
    L.insertFirst('B')
    L.display()
    L.insert(2, 'C')

    L.insert(2, 'C')
    L.insert(1,'D')
    L.insert(5,'E')
    L.display()

    L.insert(5,'F')
    L.display()
    L.delete(5)
    L.display()
    L.deleteFirst()
    L.display()