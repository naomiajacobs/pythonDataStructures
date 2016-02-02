class Tree(object):
  def __init__(self, val):
    self.val = val
    self.children = []

  def addChild(self, val):
    self.children.append(Tree(val))

  def contains(self, val, tree = None):
    if not tree:
      tree = self
    if tree.val == val:
      return True
    for child in tree.children:
      if child.val == val or tree.contains(val, child): #oh JS, I miss you so - why can't I change the self binding here?
        return True
    return False

# test = Tree('a')
# test.addChild('b')
# test.addChild('c')
# test.children[0].addChild('d')
# print(test.contains('d'))