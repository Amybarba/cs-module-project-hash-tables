class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.storage = [None] * self.capacity
        self.size = 0
        self.max_load_factor = 0.7
        self.min_load_factor = 0.2

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here

        return len(self.storage)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.size / self.capacity if self.size > 0 else 0

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.

        # Your code here
        The FNV_offset_basis is the 64-bit FNV offset basis
        value: 14695981039346656037 (in hex, 0xcbf29ce484222325).
        The FNV_prime is the 64-bit FNV prime value:
        1099511628211 (in hex, 0x100000001b3).None

        Algorithm:
        hash := FNV_offset_basis do

        for each byte_of_data to be hashed
        hash := hash x FNV_prime
        hash := hash XOR byte_of_data

        return hash

        Why bitwise?
        - Scramble thoroughly!
        - Use every bit that we are given!


        FNV_offset_basis = 14695981039346656037
        FNV_prime = 1099511628211

        byte_keys = key.encode()

        for byte in byte_keys:
            hashed_key = hashed_key * FNV_prime
            hashed_key = hashed_key ^ byte

        return hashed_key
        """

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here

        hash = 5381
        for l in key:
            hash = (hash * 33) + ord(l)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        """
        if self.get_load_factor() > .7:
            self.resize(self.capacity * 2)
            """
        # hash the key, to get the index
        index = self.hash_index(key)
        self.size += 1
        # check the index, if it's empty put a node there
        if self.storage[index] is None:
            self.storage[index] = HashTableEntry(key, value)
        # otherwise, iterate through the linked list
        else:
            current_node = self.storage[index]
            while current_node:
                # Check for the key, update value if it's there
                if current_node.key == key:
                    current_node.value = value
                    return
                # if we reach the end add a new node
                elif current_node.next:
                    current_node = current_node.next
                else:
                    current_node.next = HashTableEntry(key, value)
                    return

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here

        index = self.hash_index(key)
        # if there is a None at the index
        if self.storage[index]:

            self.size -= 1

            if self.storage[index].key == key:
                if self.storage[index].next is not None:
                    self.storage[index] = self.storage[index].next
                else:
                    self.storage[index] = None
            else:
                current_node = self.storage[index]
                while current_node.next:
                    # If the target node is the head
                    if current_node.next.key == key:
                        current_node.next = None
                    else:
                        current_node = current_node.next
        else:
            print("WARNING: sound the alarm, key not found")

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here

        index = self.hash_index(key)

        # if there's nothing at the index
        if self.storage[index]:
            current_node = self.storage[index]
            while current_node:
                if current_node.key == key:
                    return current_node.value
                else:
                    current_node = current_node.next
        else:
            return self.storage[index]


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here

        # save our old storage
        if self.get_load_factor() > self.max_load_factor:
            old_storage = self.storage.copy()
        # make a new, bigger storage!
            self.capacity = new_capacity or self.capacity * 2
            self.storage = [None] * self.capacity

        # iterate through our hashlist
            for item in old_storage:
            ## Iterate through every linked list
                while item:
                ## re-insert key, value
                    self.put(item.key, item.value)
                    item = item.next
            return
        elif self.get_load_factor() < self.min_load_factor and self.capacity > 8:
            old_storage = self.storage.copy()
            self.capacity = new_capacity or self.capacity / 2
            self.storage = [None] * self.capacity

            for item in old_storage:
                while item:
                    self.put(item.key, item.value)
                    item = item.next
            return
        else:
            return


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
