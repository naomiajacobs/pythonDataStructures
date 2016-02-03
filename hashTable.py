def getIndexBelowMaxForKey(str, max):
  hash = 0
  for idx, char in enumerate(str):
    hash = (hash<<5) + hash + ord(char)
    hash = hash & hash
    hash = abs(hash)
  return hash % max

class hashTable(object):
  def __init__(self, limit):
    self.storage = [None] * limit # must initialize with Nones to assign to partial values
    self.limit = limit
    self.size = 0

  def insert(self, key, val):
    bucketIndex = getIndexBelowMaxForKey(key, self.limit)
    if not self.storage[bucketIndex]: self.storage[bucketIndex] = []
    bucket = self.storage[bucketIndex]
    found = False
    for tuple in bucket:
      if tuple[0] == key:
        tuple[1] == val
        found = True
    if not found:
      bucket.append([key, val])

    self.size += 1
    
    if self.size >= (self.limit * .75):
      newHash = hashTable(self.limit * 2)
      for bucket in self.storage:
        if not bucket: break
        for tuple in bucket:
          newHash.insert(tuple[0], tuple[1])
      self.storage = newHash.storage
      self.limit = newHash.limit
      self.size = newHash.size

  def retrieve(self, key):
    bucketIndex = getIndexBelowMaxForKey(key, self.limit)
    if not self.storage[bucketIndex]: return None
    for tuple in self.storage[bucketIndex]:
      if tuple[0] == key: return tuple[1]
    return None

  def remove(self, key):
    temp = None
    bucketIndex = getIndexBelowMaxForKey(key, self.limit)
    if not self.storage[bucketIndex]: return None
    for idx, tuple in enumerate(self.storage[bucketIndex]):
      if tuple[0] == key:
        self.size -= 1
        temp = self.storage[bucketIndex].pop(idx)

    if self.size <= self.limit * .25:
      newHash = hashTable(self.limit / 2)
      for bucket in self.storage:
        if not bucket: break
        for tuple in bucket:
          newHash.insert(tuple[0], tuple[1])
      self.storage = newHash.storage
      self.limit = newHash.limit
      self.size = newHash.size

    return temp[0]

# test = hashTable(4)
# test.insert('cat', 'kitten')
# test.insert('dog', 'puppy')
# print(test.retrieve('dog'))
# test.remove('dog')
# print(test.retrieve('dog'))
# test.insert('kangaroo', 'joey')
# test.insert('rabbit', 'bunny')
# print(test.limit)
