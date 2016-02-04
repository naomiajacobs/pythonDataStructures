import math

class Heap(object):
  def __init__(self, type):
    self.heap = []
    self.type = type

  def __swapElements(self, firstI, secondI):
    self.heap[firstI], self.heap[secondI] = self.heap[secondI], self.heap[firstI]

  def __siftDown(self):
    heap = self.heap
    index = 0
    childI = self.__getSwapChild(index)
    while childI < len(self.heap) and self.__compare(index, childI):
      self.__swapElements(childI, index)
      index = childI
      childI = self.__getSwapChild(index)

  def __siftUp(self):
    index = len(self.heap) - 1
    parentI = self.__getParentI(index)
    while parentI >= 0 and self.__compare(parentI, index):
      self.__swapElements(index, parentI)
      index = parentI
      parentI = self.__getParentI(index)

  def __getSwapChild(self, index):
    child1I = 2 * index + 1
    child2I = 2 * index + 2
    # check to see if they exist
    if child1I > len(self.heap) - 1: return len(self.heap)

    if child2I > len(self.heap) - 1: return child1I

    child1 = self.heap[child1I]
    child2 = self.heap[child2I]

    if self.type == 'max':
      return child1I if child1 > child2 else child2I
    else:
      return child1I if child1 < child2 else child2I

  def __getParentI(self, index):
    return int(math.floor((index - 1)/2))

  def __compare(self, parentI, childI):
    # returns true if a swap should be made, false if not
    parentVal, childVal = self.heap[parentI], self.heap[childI]
    if self.type == 'max':
      return childVal > parentVal
    else:
      return childVal < parentVal

  def peek(self):
    return self.heap[0]

  def insert(self, val):
    self.heap.append(val)
    self.__siftUp()

  def extractMax(self):
    temp = self.heap.pop(0)
    self.__siftDown()
    return temp

test = Heap('max')
test.insert(73)
test.insert(3)
print 'should be 73: ', test.peek()
test.insert(38)
test.insert(123)
print 'should be 123: ', test.peek()
test.insert(234)
print 'should be 234: ', test.peek()
print 'should be 234: ', test.extractMax()
print 'new top should be 123: ', test.peek()