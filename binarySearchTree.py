class binarySearchTree(object):
  def __init__(self, val):
    self.left = None
    self.right = None
    # self.parent = None
    self.val = val

  def insert(self, val):
    # side = 'left' if self.val > val else 'right'
    # if self[side] == None:
    #   self[side] = binarySearchTree(val)
    # else:
    #   self[side].insert(val)
    if self.val > val:
      if self.left == None:
        self.left = binarySearchTree(val)
      else:
        self.left.insert(val)
    else:
      if self.right == None:
        self.right = binarySearchTree(val)
      else:
        self.right.insert(val)

  def contains(self, val):
    if self.val == val: return True
    if self.left and self.left.contains(val): return True
    if self.right and self.right.contains(val): return True
    return False

  def depthFirstLog(self, cb):
    cb(self)
    if self.left: self.left.depthFirstLog(cb)
    if self.right: self.right.depthFirstLog(cb)

def printNode(node):
  print node.val

# test = binarySearchTree(50)
# test.insert(25)
# test.insert(75)
# test.insert(23)
# test.insert(77)
# test.insert(33)
# test.insert(99)
# print('contains, should be false: ', test.contains(22))
# print('contains, should be true: ', test.contains(99))
# test.depthFirstLog(printNode)