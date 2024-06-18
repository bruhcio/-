class DListNode:
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next

class DListType:
    def __init__(self):
        self.front = self.rear = None ##head랑 tail로 해도 상관없지만 그냥 이걸로 ## 아무 연결이 되지 않은 상태로 front, rear 생성
        self.size = 0

    def addFront(self, data):
        node = DListNode(data, None, self.front) ##prev = 맨 처음으로 들어가니까 아무것도 없음

        if self.size == 0:
            self.front = self.rear = node ##만약 사이즈가 0이면 맨 처음도 나고 맨 마지막도 나다

        else:
            self.front.prev = node
            self.front = node

        self.size += 1

    def addRear(self, data):
        node = DListNode(data, self.rear, None)  ## prev가 self.rear인 이유는 이걸 삽일했을 때 그 전이  지금의 나여야 하니까

        if self.size == 0:  ## 여기도 똑같이 사이즈가 0일 때를 생각해야한다.
            self.front = self.rear = node

        else:
            self.rear.next = node   ##  마지막의 다음은 나이다.
            self.rear = node        ##  그리고 다시 마지막 즉 맨 뒤는 나이다.

        self.size += 1

    def addPos(self, pos, data):
        node = DListNode(data, None, None) ##None이라는 것은 아직 미정이라는 뜻

        if pos == 1:
            self.addFront(data)
        elif pos == self.size + 1:  ## 마지막이라는 뜻
            self.addRear(data)
        else:
            p = self.front
            for x in range(1, pos): ## x가 1로 시작하게 하든지 아니면 pos -1까지 움직이게 하면 된다.
                p = p.next

            node.prev = p.prev
            node.next = p

            p.prev.next = node
            p.prev = node
            self.size += 1

    def deleteFront(self):
        if self.size != 0:
            data = self.front.data          ##가장 앞에 거 삭제하기 전에 기록해두기
            self.front = self.front.next    ##지금 맨 앞의 값은 그 다음의 값이 된다. 즉 삭제

            if self.front == None:          ## 그 전에 유령 큐 같은 느낌?
                self.rear = None
            else:
                self.front.prev = None
            self.size -= 1
            return data

    def deleteRear(self):
        if self.size != 0:
            data = self.rear.data
            self.rear = self.rear.prev

            if self.rear == None:
                self.front = None
            else:
                self.rear.next = None
            self.size -= 1
            return data

    def deltePos(self, pos): ### 이거 만들기
        if pos == 1:    # 일단 1번이면 만들어 놓은 거 활용
            self.deleteFront()
        elif pos == self.size + 1:  # 마지막이면 만든 거 사용
            self.deleteRear()
        else:                       #
            p = self.front
            for i in range(1, pos): # 1부터 pos까지 p값을 미뤄서 pos의 위치로 하게 함
                p = p.next          # 이 때 pos는 pos위치값

            data = p.data           # pos위치의 데이터 값
            p.prev.next = p.next    # 여기서 p = p.next라고 해버리면 p 값이 변해버려서 뒤에 사용하기 힘듬
                                    # 그리고 p값 이전의 데이터의 다음은 p 값이 아닌 현재 p값의 다음 거 라고 나타내는 것이다.
            p.next.prev = p.prev
                                    # 여기서도 p값 다음 데이터 이전은 p값이 아니라 현재 p값의 이전 데이터임을 명시
                                    # 유령 값 없애는 거? -> 일단 찍어보니까 이거 않하면 유령 값이 있음
            self.size -= 1
            return data

    def display(self):
        p = self.front

        while p != None:
            print(f'{p.data} <-> ', end = '')
            p = p.next

        print('\b\b\b\b    ') ##\b는 뒤로 지운다. <-> 삭제하는 거

if __name__ == '__main__':
    DL = DListType()

    DL.addFront('A')
    DL.addFront('B')
    DL.display()

    DL.addRear('C')
    DL.display()

    DL.addFront('D')
    DL.display()

    DL.addRear('E')
    DL.display()

    DL.addPos(3, 'F')
    DL.display()

    print(f'{DL.deleteFront()} is deleted : ', end= '')
    DL.display()

    print(f'{DL.deleteRear()} is deleted : ', end='')
    DL.display()

    print(f'{DL.deltePos(2)} is deleted : ', end='')
    DL.display()