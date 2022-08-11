
"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 

Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
"""


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_usage = {}
        self.lru = {}
        return None

    def get(self, key: int) -> int:
        
        if key in self.lru.keys():
            # self.key_usage[key] = self.key_usage[key]+1 if key in self.key_usage.keys() else 1
            self.key_usage[key] = max(self.key_usage.values())+1
            print(f'GET {key} LRU - ',self.lru, self.key_usage)
            return self.lru[key]
        print(f'GET {key} LRU - ',self.lru, self.key_usage)
        return -1

    def put(self, key: int, value: int) -> None:
        # If LRU capacity is already reached
        if (not key in self.lru.keys()) and (len(self.lru.keys())>=self.capacity):
            # Delete the least used key
            min_value = min(self.key_usage.values())
            least_used_key = [kk for kk in self.key_usage.keys() if self.key_usage[kk]==min_value] 
            print(f'least_used_key:{least_used_key}')
            # delete least used key
            del self.lru[least_used_key[0]]
            del self.key_usage[least_used_key[0]]
            # reset the key_usage stats
            for k in self.key_usage.keys(): self.key_usage[k] = 1

        self.lru[key] = value
        self.key_usage[key] = max(self.key_usage.values())+1 if len(self.key_usage.values())>0 else 1
        print(f'PUT ({key,value}) LRU - ',self.lru, self.key_usage)
        return None
# Your LRUCache object will be instantiated and called as such:
result = []
obj = LRUCache(2)
result.append(None)
obj.put(2, 1)
result.append(None)
obj.put(2, 2)
result.append(None)
param_1 = obj.get(2)
result.append(param_1)
obj.put(1, 1)
result.append(None)
obj.put(4, 1)
result.append(None)
param_2 = obj.get(2)
result.append(param_2)
print(result)
print("------")



# Approach 2 
class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.data={}

    def get(self, key: int) -> int:
        if key not in self.data: return -1
		#item recently accessed need to be sent at last of dict, pop and reassign 
        self.data[key]=self.data.pop(key)
        return self.data[key]
    
    def put(self, key: int, value: int) -> None:
        if key in self.data:
			#item updated recently need to be sent at last of dict, pop and update
            self.data.pop(key)
            self.data[key]=value
            return
		#if capacity is reached, we removed first item of dict. which is always least used
        if self.cap==len(self.data): self.data.pop(next(iter(self.data)))
        self.data[key]=value
        return
