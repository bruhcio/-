class Node:
    def __init__(self,data,next): #next는 오른쪽, previous = 왼쪽
        self.data = data
        self.next = next # 원형이랑 다르게 순환이 아님

class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def isEmpty(self):
        return self.front == None

    def enqueue(self, data):
        node = Node(data, None)
        if self.isEmpty():
            self.front = self.rear = node#노드의 마지막도 나야.
        else:
            self.rear.next = node ###일단 잘 모르겠음
            self.rear = node#내가 전체 리스트의 마지막 노드가 된다.
        self.size += 1

    def dequeue(self):
        if not self.isEmpty():
            data = self.front.data
            self.front = self.front.next
            p = self.front
            p = self.front.next

            if p == None:
                self.rear = None
            self.size -= 1
            return data
        else:
            print('No Elements')

    def display(self):
        if self.isEmpty():
            print("No Elements")
            return

        p = self.front #맨 처음 노드를 가리킴
        while p:
            if p.next:
                print('[%s] -> ' %p.data, end = '')
            else:
                print('[%s]' % p.data, end='')
            p = p.next
        print()

if __name__ == "__main__":
    Q = LinkedQueue()

    Q.enqueue('A')
    Q.display()
    Q.enqueue('B')
    Q.display()
    Q.enqueue('C')
    Q.display()

    Q.dequeue()
    Q.display()
