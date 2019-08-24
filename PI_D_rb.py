n, k, a = map(int, input().split())
m = int(input())
x = list(map(int, input().split()))

ship_count = (n+1) // (a+1)
class Node:
    def __init__(self, val):
        self.val = val
        self.left_pos = 1
        self.right_pos = n
        self.left = None
        self.right = None
        self.parent = None
        self.color = 1

    def eval_diff(self):
        global ship_count, reduced
        ship_count_was = (self.right_pos - self.left_pos + 1 + 1) // (a + 1)
        ship_count_became  = (self.val - self.left_pos + 1) // (a + 1)
        ship_count_became += (self.right_pos - self.val + 1) // (a + 1)

        ship_count -= ship_count_was - ship_count_became
        self.ship_count = ship_count_became

    def check_rbtree(self):
        parent = self.parent
        if parent == None:
            self.color = 0
            return
        if parent.color == 0:
            return
      
        grand = parent.parent  
        if grand == None:
            self.parent.color = 0
            return 

        uncle = grand.left
        if uncle == parent:
            uncle = grand.right

        if uncle == None or uncle.color == 0:
            if uncle == grand.left and self == parent.left \
               or uncle == grand.right and self == parent.right:

                parent.rotate(self)
                grand.color = 1
                self.color = 0
                grand.rotate(self)

            else:
                grand.color = 1
                parent.color = 0
                grand.rotate(parent)
        else:
            uncle.color = 0
            parent.color = 0
            grand.color = 1
            grand.check_rbtree()

    def rotate(self, node):
        if self.left != node and self.right != node:
            raise Exception()
            
        if self.parent != None:
            if self.parent.left == self:
                self.parent.left = node
            elif self.parent.right == self:
                self.parent.right = node
            else:
                raise Exception()

        node.parent = self.parent
        self.parent = node

        if self.left == node:
            self.left = node.right
            if self.left != None:
                self.left.parent = self
            node.right = self
        elif self.right == node:
            self.right = node.left
            if self.right != None:
                self.right.parent = self
            node.left = self

    def add(self, node):
        if (node.val < self.val):
            node.right_pos = self.val - 1
            if self.left == None:
                self.left = node
                self.left.parent = self
                self.left.eval_diff()
                self.left.check_rbtree()
            else:
                self.left.add(node)
        elif (node.val > self.val):
            node.left_pos = self.val + 1
            if self.right == None:
                self.right = node
                self.right.parent = self
                self.right.eval_diff()
                self.right.check_rbtree()
            else:
                self.right.add(node)

    def traverse(self, deq):
        if self.left != None:
            self.left.traverse(deq)
        deq.append(self.val)
        if self.right != None:
            self.right.traverse(deq)

    def traverse_depth(self, deq, level = 0):
        if self.left != None:
            self.left.traverse_depth(deq, level + 1)
        deq.append(level)
        if self.right != None:
            self.right.traverse_depth(deq, level + 1)


class Tree:
    def __init__(self):
        self.root = None

    def add(self, val):
        node = Node(val)
        if self.root == None:
            self.root = node
            self.root.eval_diff()
            self.root.check_rbtree()
        else:
            self.root.add(node)
            while self.root.parent != None:
                self.root = self.root.parent

    def traverse(self):
        deq = []
        if self.root != None:
            self.root.traverse(deq)
        return deq

    def traverse_depth(self):
        deq = []
        if self.root != None:
            self.root.traverse_depth(deq, 1)
        return deq
    
tree = Tree()
for i in range(len(x)):
    tree.add(x[i])
    print(tree.traverse_depth())
    if ship_count < k:
        print(i+1)
        break
else:
    print(-1)