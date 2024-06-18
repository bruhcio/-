class Node:
    def __init__(self,data,next): #next는 오른쪽, previous = 왼쪽
        self.data = data
        self.next = next

class CircularQueue:
    def __init__(self):
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.tail == None

    def enqueue(self, data): #== insertLast임 큐이니까
        node = Node(data, None) #아직 data값이 들어가지 않았으니까 none을 하자 - 일단 노드는 만든 상태이다.
        #아무것도 없는 노드에 처음 삽입해주면 노드가 '자신이 처음이자 마지막 노드이다'라는 것을 표현해줘야 함
        #반대로 1개만 남았을 때 노드 삭제 하려고 하면 '자신이 처음이자 마지막 노드임'을 알려야 함
        #그러므로 테스트할 때 1개만 남았을 때 삭제를 해보고 아무것도 있지 않은 상태에 삽입을 해보자
        #유령 노드??? - e-d-e 해보기

        if self.isEmpty():
            node.next = node #만들어진 노드의 다음은 나야 - 즉 내가 맨 처음이야
            self.tail = node #노드의 마지막도 나야.
        else:
            node.next = self.tail.next ###일단 잘 모르겠음
            self.tail.next = node
            self.tail = node #내가 전체 리스트의 마지막 노드가 된다.

        self.size += 1

    def dequeue(self):
        if not self.isEmpty():
            p = self.tail
            q = p.next
            data = q.data

            if p == q:
                self.tail = None
            else:
                p.next = q.next

            self.size -= 1
            return data
        else:
            print('No Elements')

    def display(self):
        if self.isEmpty():
            print("No Elements")
            return

        p = self.tail.next #맨 처음 노드를 가리킴
        for i in range(self.size):
            print('[%s] -> ' %p.data, end = '')
            p = p.next

        print('\b\b\b')

if __name__ == "__main__":
    Q = CircularQueue()

    Q.enqueue('A')
    Q.display()
    Q.enqueue('C')
    Q.display()
    Q.enqueue('B')
    Q.display()

    Q.dequeue()
    Q.display()




