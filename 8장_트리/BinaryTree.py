## 일반 트리임 이진 트리 아니다. - 복잡하려나??
## 트리에서 노드들의 방문 순서로 옳은 것은?
import queue
class TreeNode:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def preOrder(self, node):           #전위 순회 == 기본적인 트리
        if node is not None:
            print('[%c] ' %node.data)
            self.preOrder(node.left)
            self.postOrder(node.right)

    def inOrder(self, node):            #중위 순회 == 맨 아래 서브 노드부터 나오고
        if node != None:
            self.inOrder(node.left)
            print('[%c] ' %node.data)
            self.inOrder(node.right)

    def postOrder(self, node):          #후위 순회 ==  맨 아래 서브 노드(왼쪽 오른쪽 다 ) 건들이고 올라감
        if node != None:
            self.postOrder(node.left)
            self.postOrder(node.right)
            print('[%c] ' %node.data)

    def levelOrder(selfself, node):
        ## 여기 부분에 Q 아마 원형 큐 사용해야 할 것 같은데 다른 사람 꺼 봐보기
        Q = queue.Queue()
        Q.put(node)

        while not Q.empty():
            node = Q.get()
            print('[%c]' %node.data, end=' ')

            if node.left != None:
                Q.put(node.left)
            if node.right != None:
                Q.put(node.right)

    def nodeCount(self, node):
        count = 0
        if node != None:
            count = (1 + self.nodeCount(node.left) \
                     + self.nodeCount(node.right))

        return count

    def isExternal(self, node):
        return node.left == None and node.right == None

    def leafCount(self, node):
        count = 0
        if node != None:
            if self.isExternal(node):
                return 1
            else:
                count = (1 + self.leafCount(node.left) \
                             + self.leafCount(node.right))
        return count

    def getHeight(self, node):
        if node == None:
            return 0

        return max(self.getHeight(node.left),self.getHeight(node.right)) + 1

if __name__ == "__main__":
    T = BinaryTree()

    n6 = TreeNode('F')
    n5 = TreeNode('E')
    n4 = TreeNode('D')
    n3 = TreeNode('C', n6)
    n2 = TreeNode('B', n4, n5)
    n1 = TreeNode('A', n2, n3) # 데이터와, 연결된 노드 == 그런데 항상 생각하야 하는게 트리에서는 왼쪽이 먼저 나오는 거

    print('Pre: ', end = ' '); T.preOrder(n1); print()
    print('In: ', end=' '); T.inOrder(n1); print()
    print('Post: ', end=' '); T.postOrder(n1); print()
    print('Level: ', end=' '); T.levelOrder(n1); print()

    print("Node Count: %d" %T.nodeCount(n1))
    print("Leaf Count: %d" % T.leafCount(n1))


####pdf에 나와 있는 모스코드 부분 == 트리 구조랑 비슷하다.