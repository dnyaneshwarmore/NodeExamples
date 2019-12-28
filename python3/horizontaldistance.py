#node definition
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


#use queue to perform level order traversal 
def levelArray(root, l ,r):
    print("inside the function ")
    queue = []
    if (root == None):
        return -1, -1
    ncnt = 0
    hd = 0
    flg= False
    queue.append(root)
    print("before the loop")
    while len(queue) is not 0:
        val = queue.pop(0)
        if (flg and val == None):
            ncnt+=1
            hd+=1
            continue
            
        if (val.data == r):
            break
        if (flg):
            hd+=1
        if val.data == l:
            flg = True

        if (val.left):
            queue.append(val.left)
        else:
            queue.append(None)
        if (val.right):
            queue.append(val.right)
        else:
            queue.append(None)
    return ncnt, hd


def main():
    root = Node(5)
    root.left = Node(2)
    root.left.left = Node(7)
    root.left.left.left = Node(9)
    root.right = Node(3)
    root.right.right = Node(1)
    root.right.right.left = Node(4)
    root.right.right.right = Node(6)
    print(levelArray(root, 7, 1))


def if __name__ == "__main__":
    main()
