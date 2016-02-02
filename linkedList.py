class Node(object):
  def __init__(self, val):
    self.val = val
    self.next = None
    self.prev = None

class DoublyLinkedList(object):
  def __init__(self):
    self.head = None
    self.tail = None

  def insertAtHead(self, val):
    node = Node(val)
    if self.head == None:
      self.head = self.tail = node
    else:
      self.head.prev = node
      node.next = self.head
      self.head = node

  def insertAtTail(self, val):
    node = Node(val)
    if self.tail == None:
      self.head = self.tail = node
    else:
      self.tail.next = node
      node.prev = self.tail
      self.tail = node

  def shift(self):
    temp = self.head
    self.head = self.head.next
    self.head.prev = None
    temp.next = None
    return temp.val

  def pop(self):
    if self.tail == None:
      return None
    else:
      temp = self.tail
      if self.head != self.tail:
        self.tail = self.tail.prev
        self.tail.next = None
        temp.prev = None
        return temp.val
      else:
        self.head = None
        self.tail = None
        return temp.val

  def contains(self, val):
    node = self.head
    while node:
      if node.val == val:
        return True
      node = node.next
    return False


# test = DoublyLinkedList()
# test.insertAtHead('hi')
# print('should be true: ', test.contains('hi'))
# test.insertAtHead('there')
# test.insertAtTail('friend')
# print('should be false: ', test.contains('friend'))




