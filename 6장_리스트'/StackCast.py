from ListType import ListType

S = ListType() #리스트 타입 객체하나 소환

def push(data):
    S.insertFirst(data)

def pop():
    return S.deleteFirst() #왜??? 왜 delete first?

push('A')
S.display()
push('B')
S.display()

print('[%s] is deleted' % pop())
S.display()