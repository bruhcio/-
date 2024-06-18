M = 13
table = [0] * M

def hashFn(key):
    return key * M

def hashFn2(key): #2중 해싱
    return 11 - (key % 11) # m보다 작은 소수에서 빼기

def getLinear(v, i):
    return (v + i) % M

def getQuadratic(v, i):
    return (v + i * i) % M

def getDouble(v, i, key):
    return (v + i * hashFn2(key)) % M

def insert(key):
    v = hashFn(key) #
    i = 0 # 내가 열어본 횟수

    while i < M:
        b = getLinear(v, i) #일단 이걸로 작성했었는데 getQuadratic으로 받기 # 그 다음에는 getLinear로 다시 해보기
        #b = getQuadratic(v, i)
        #b = getDouble(v, i , key) ##2중 해싱할 떄 만듬

        if table[b] == 0:
            table [b] = key
            return

        else:
            i += 1

def search(key):
    v = hashFn(key) #
    i = 0 # 내가 열어본 횟수

    while i < M:
        b = getLinear(v, i) #일단 이걸로 작성했었는데 getQuadratic으로 받기 # 그 다음에는 getLinear로 다시 해보기
        #b = getQuadratic(v, i)
        #b = getDouble(v, i , key) ##2중 해싱할 떄 만듬

        print('[%d]' %table[b], end = '')

        if table[b] == 0:
            return 

        elif table[b] == key: # insert만들면서 만듬
            return table [b] # insert만들면서 만듬

        else:
            i += 1

def delete(key):
    v = hashFn(key) #
    i = 0 # 내가 열어본 횟수

    while i < M:
        b = getLinear(v, i) #일단 이걸로 작성했었는데 getQuadratic으로 받기 # 그 다음에는 getLinear로 다시 해보기
        #b = getQuadratic(v, i)
        #b = getDouble(v, i , key) ##2중 해싱할 떄 만듬

        print('[%d]' %table[b], end = '')

        if table[b] == 0:
            print('No key to delete')
            return
        elif table[b] == key: # insert만들면서 만듬
            table [b] = -1
            return
        else:
            i += 1


def display():
    print()
    print('Bucket   Key')
    print('============')

    for i in range(M):
        print('HT[%2d] : %2d' %(i, table[i]))


if __name__ == "__main__":
    data = [45,27,88,9,71,60,46,38,24]
    for d in data:
        print('h(%2d) = %2d' %(d, hashFn(d)), end = ' ')
        insert(d)
        print(table)

    display()
    print()
    print('Search(46) --> ', search(46))
    print('Search(39) --> ', search(39))

    delete(60); display() #해싱 테이블에서는 삭제 연산이 불가? -> 0이란 처음부터 비어있다. -> 애초에 처믕부터 누구도 기숙사 방을 배정받은 적이 없다.
                          #빈 방 구분 해야함 1. 처음부터 빈 방, 2. 있다가 없어진 빈 방
    print('Search(46) --> ', search(46))