from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.cache = OrderedDict()

    def get(self, key):
        if key in self.cache:
            value = self.cache[key]
            self.remove(key)
            self.cache[key] = value
            return value
        else:
            return -1

    def remove(self, key):
        del self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.remove(key)
            self.cache[key] = value
        elif self.size < self.capacity:
            self.cache[key] = value
            self.size += 1
        else:
            self.cache.popitem(last=False)
            self.cache[key] = value
            self.size += 1


obj = LRUCache(2)

print(obj.put(2, 1))
print(obj.cache)

print(obj.put(1, 1))
print(obj.cache)


print(obj.put(2, 3))
print(obj.cache)

print(obj.put(4, 1))
print(obj.cache)

print(obj.get(1))
print(obj.cache)


print(obj.get(2))
print(obj.cache)


print(obj.get(1))
print(obj.cache)

print(obj.get(2))
print(obj.cache)
