class Treenode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root == None:
        return Treenode(key)

    if key < root.key:                           #들어온 수가 루트보다 작으면
        root.left = insert(root.left, key)       #들어온 수는 루트의 왼쪽이 된다.
    elif key > root.key:                         #들어온 수가 루트보다 크면
        root.right = insert(root.right, key)     #들어온 수는 루트의 오른쪽이 된다.
    else: #없어도 상관 없음
        pass
    return root

def getMinNode(root):                            #case3에서 사용 됨
    while root != None and root.left != None:
        root = root.left

    return root


def delete(root, key):
    if root == None:
        return None

    if key < root.key:                           #들어온 수가 루트보다 작으면
        root.left = delete(root.left, key)       #들어온 수는 루트의 왼쪽이 된다.
    elif key > root.key:                         #들어온 수가 루트보다 크면
        root.right = delete(root.right, key)     #들어온 수는 루트의 오른쪽이 된다.
    else:
        if root.left == None:                    #case1 : 왼 쪽 자식이 없는 경우
            return root.right
        elif root.right == None:                 #case2 : 자식이 하나 = 노드가 오른 쪽만 있는 경우?
            return root.left
        else:
            succ = getMinNode(root.right)        #case3 :
            root.key = succ.key
            root.right = delete(root.right, succ.key)

    return root

def inOrder(root):
    if root:
        inOrder(root.left)
        print('%2d ' %root.key, end = '')
        inOrder(root.right)


def display(root, msg):
    print(msg,end = '')
    inOrder(root)
    print()

if __name__ == "__main__":
    root = None
    data = [35, 18, 7, 26, 3, 22, 30, 12, 26, 68, 99]

    for key in data:
        root = insert(root, key)
        display(root,'[insert %2d]' %key)
    print()
    #
    # root = delete(root, 30)
    # display(root, '[Delete 30] : ')
    #
    # root = delete(root, 26)
    # display(root, '[Delete 26] : ')

    root = delete(root, 18)
    display(root, '[Delete 18] : ')

