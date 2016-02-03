class Tree(object):
  def __init__(self, val):
    self.val = val
    self.children = []
    self.parent = None

  def addChild(self, val):
    child = Tree(val)
    child.parent = self
    self.children.append(child)

  def contains(self, val, tree = None):
    if not tree:
      tree = self
    if tree.val == val:
      return True
    for child in tree.children:
      if child.val == val or tree.contains(val, child):
        return True
    return False

  def removeFromParent(self):
    if not self.parent: return False
    for idx, child in enumerate(self.parent.children):
      if child.val == self.val:
        self.parent.children.pop(idx)
        break
    self.parent = None