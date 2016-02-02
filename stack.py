class Stack(object):

  def __init__(self):
    self._storage = []

  def push(self, val):
    self._storage.append(val)

  def pop(self):
    if len(self._storage) > 0:
      temp = self._storage.pop()
      return temp
    else:
      return 'empty'

# test = Stack()
# test.push('there')
# test.push('friend')
# print(test.pop())
# print(test.pop())
# print(test.pop())