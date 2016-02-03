class Graph(object):
  def __init__(self):
    self.storage = {}
    self.edges = []

  def addNode(self, val):
    self.storage[val] = val
    print self.storage
    return val

  def contains(self, val):
    for node in self.storage:
      # keys should be values, so this should work
      if node == val: return True
    return False

  def addEdge(self, fromNode, toNode):
    if self.contains(fromNode) and self.contains(toNode):
      if [fromNode, toNode] in self.edges:
        # edge already exists
        return None
      else:
        self.edges.append([fromNode, toNode])
    else:
      # edges don't exist
      return None

  def hasEdge(self, fromNode, toNode):
    if [fromNode, toNode] in self.edges: return True
    return False

  def removeEdge(self, fromNode, toNode):
    temp = None
    for index, edge in enumerate(self.edges):
      if edge == [fromNode, toNode]:
        temp = self.edges.pop(index)
        break
    return temp.val

  def removeNode(self, node):
    if node not in self.storage: return None
    temp = None
    del self.storage[node.val]
    for index, edge in enumerate(self.edges):
      if edge[0] == node or edge[1] == node:
        temp = self.edges.pop(index)
    return temp

  def forEachNode(self, cb):
    for node in self.storage:
      cb(node)


test = Graph()
node1 = test.addNode('a')
node2 = test.addNode('b')
node3 = test.addNode('c')
node4 = test.addNode('d')
test.addEdge(node1, node2)
test.addEdge(node2, node3)
test.addEdge(node4, node1)
print('contains, should be true: ', test.contains(node1));
print('should be true: ', test.hasEdge(node1, node2))
print('should be false: ', test.hasEdge(node3, node4))
