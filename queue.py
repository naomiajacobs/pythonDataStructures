class Queue(object):

  def __init__(self):
    self.storage = []

  def enqueue(self, val):
    self.storage.append(val)

  def dequeue(self):
    if len(self.storage) > 0:
      return self.storage.pop(0)
    else:
      return 'empty'

# test = Queue()
# test.enqueue('hi')
# test.enqueue('there')
# print(test)
# print(test.dequeue())
# print(test.dequeue())
# print(test.dequeue())