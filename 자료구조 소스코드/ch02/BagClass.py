# 2.10 도전 문제

# 1.   
class Bag:
    def __init__( self ):
        self.bag = []

    def contains(self, e) :
        return e in self.bag

    def insert(self, e) :
        self.bag.append(e)

    def remove(self, e) :
        self.bag.remove(e)

    def count(self):
        return len(self.bag)


# 테스트 프로그램 
myBag = Bag()
myBag.insert('휴대폰')
myBag.insert('지갑')
myBag.insert('손수건')
myBag.insert('빗')
myBag.insert('자료구조')
myBag.insert('야구공')
print('내 가방속의 물건:', myBag.bag)

myBag.insert('빗')
myBag.remove('손수건')
print('내 가방속의 물건:', myBag.bag)



