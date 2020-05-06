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


    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        index = self.hash_index(key)
        current = self.storage[index]

        if current is None:
            self.storage[index] = HashTableEntry(key, value)
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

    def resize(self, capacity=None):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        if capacity is not None:
            self.capacity = capacity
        else:
            self.capacity = self.capacity * 2
        tempStor = self.storage

        self.storage = [None] * self.capacity

        for i in tempStor:
            r = i

            while r is not None:
                prev = r
                r = prev.next
                prev.next = None

                self.put(prev.key, prev.value)


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
