import queue


class TreeNode: ##트리 노드 선언, 들어갈 거 data = 데이터 값, left = 왼쪽 노드, right = 오른쪽 노드
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def preOrder(self, node):
        if node != None:
            print(f'{node.data}')
            self.preOrder(node.left)
            self.preOrder(node.right)
    def inOrder(self, node):
        if node != None:
            self.inOrder(node.left)
            print(f'{node.data}')
            self.inOrder(node.right)

    def postOrder(self, node):
        if node != None:
            self.postOrder(node.left)
            self.postOrder(node.right)
            print(f'{node.data}')
    
    def levelOrder(self, node):
        Q = queue.Queue()
        Q.put(node)

        while not Q.empty():
            node = Q.get()
            print (f'{node.data}', end = '')

            if node != None:
                Q.put(node.left)
