class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None



class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    def __init__(self,capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.size = 0
        self.load = 0

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """
        h = 14695981039346656037
        for b in str(key).encode():
            h *= 1099511628211
            h ^= b
        return h

    def _hash(self, key):
        return hash(key)

    def djb2(self, key):
        """
        DJB2 32-bit hash function
        Implement this, and/or FNV-1.
        """
        hash = 5381
        for i in key:
            hash = ((hash << 5 ) + hash) + ord(i)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        #return self.djb2(key) % self.capacity
        #return self._hash(key) % self.capacity

    def get_load(self):
        load = float(self.size / len(self.storage))
        return load


    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        if self.get_load() >= 0.7:
            self.resize()

        index = self.hash_index(key)
        current = self.storage[index]
        
       
        if current is None:
            self.storage[index] = HashTableEntry(key, value)
            self.size += 1 
            return
        if current.key == key:
            current.value = value
            return
        while current.next is not None:
            if current.next.key == key:
                current.next.value = value
                return 
            current = current.next
        current.next = HashTableEntry(key, value)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        current = self.storage[index]
        #self.storage[index] = None
        while current.key != key:
            if current.next is None:
                return False
            current = current.next

        curvalue = None
        if current.key == key:
            curvalue = current.value
            current.value = None

        return curvalue
#         my_hash_index = self.hash_index(key)
# ​
#         node = self.storage[my_hash_index]
#         prev = None
# ​
#         while node is not None and node.key != key:
#             prev = node
#             node = node.next
# ​
#         if node is None:
#             print('Sorry, I cannot find that key.')
# ​
#         else:
#             self.size -= 1
#             if self.load < 0.2:
#                 self.desize()
#             if prev is None:
#                 self.storage[my_hash_index] = node.next
#             else:
#                 prev.next = prev.next.next



    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        current = self.storage[index]
        if current is None:
            return False
        while current.key != key:
            if current.next is None:
                return False
            current = current.next

        return current.value

        # if self.storage[index] == None:
        #     return None
        # else:
        #     return self.storage[index].value

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        self.storage = self.storage + [None] * int(self.capacity)
        return self.storage
        print(self.storage)

    def desize(self):
        old_array = self.storage
        self.capacity = self.capacity / 2
        new_array = [None] * int(self.capacity)
        self.storage = new_array
        for e in old_array:
            if e is not None:
                self.put(e.key, e.value)
                e = e.next



if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    for i in ht.storage:
        print(f"self.storage>>>>>{i}")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
