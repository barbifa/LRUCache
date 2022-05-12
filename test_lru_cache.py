import unittest
from lru_cache import LRUCache


class TestLRUCache(unittest.TestCase):

    def test_get_value(self):
        obj = LRUCache(3)
        obj.cache[1] = 4
        obj.cache[2] = 5
        obj.cache[4] = 6
        result = obj.get(2)
        self.assertEquals(result, 5)
        result = obj.get(9)
        self.assertEquals(result, -1)

    def test_remove_item(self):
        obj = LRUCache(3)
        obj.cache[1] = 4
        obj.cache[2] = 5
        obj.cache[4] = 6

        d2 = {1: 4, 4: 6}
        obj.remove(2)
        self.assertDictEqual(obj.cache, d2)

    def test_put_item(self):
        obj = LRUCache(3)
        obj.cache[1] = 4
        obj.cache[2] = 5
        obj.cache[4] = 6
        obj.size = 3
        # when the key is already in the cache
        obj.put(2, 9)
        d2 = {1: 4, 4: 6, 2: 9}
        self.assertDictEqual(obj.cache, d2)

        obj = LRUCache(3)
        obj.cache[1] = 4
        obj.cache[2] = 5
        obj.cache[4] = 6
        obj.size = 3

        # when over capacity
        obj.put(3, 4)
        d2 = {2: 5, 4: 6, 3: 4}
        print('hereeeeee')
        print(obj.cache)
        self.assertDictEqual(obj.cache, d2)

        obj = LRUCache(4)
        obj.cache[1] = 4
        obj.cache[2] = 5
        obj.cache[4] = 6
        obj.size = 3

        # when there is space and its a new key
        obj.put(3, 4)
        d2 = {1: 4, 2: 5, 4: 6, 3: 4}
        self.assertDictEqual(obj.cache, d2)


if __name__ == '__main__':
    unittest.main()
