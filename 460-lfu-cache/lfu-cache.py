class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_val_freq = {}  # key -> (value, frequency)
        self.freq_to_nodes = defaultdict(OrderedDict)  # freq -> OrderedDict(key -> None)
        self.min_freq = 0  # Tracks the minimum frequency

    def _update_freq(self, key):
        """Helper function to update frequency of a key in O(1)"""
        value, freq = self.key_to_val_freq[key]
        
        # Remove key from current frequency list
        del self.freq_to_nodes[freq][key]
        if not self.freq_to_nodes[freq]:  # If empty, delete the frequency bucket
            del self.freq_to_nodes[freq]
            if self.min_freq == freq:  # If this was the minimum frequency, update it
                self.min_freq += 1
        
        # Add key to the next frequency list
        self.freq_to_nodes[freq + 1][key] = None
        self.key_to_val_freq[key] = (value, freq + 1) 

    def get(self, key: int) -> int:
        if key not in self.key_to_val_freq:
            return -1
        
        self._update_freq(key)  # Increase frequency count
        return self.key_to_val_freq[key][0]
        

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_to_val_freq:
            # Update value and frequency
            self.key_to_val_freq[key] = (value, self.key_to_val_freq[key][1])
            self._update_freq(key)
        else:
            # Eviction: Remove least frequently used key if capacity is reached
            if len(self.key_to_val_freq) >= self.capacity:
                # Get LRU key from the least frequency list
                lfu_key, _ = self.freq_to_nodes[self.min_freq].popitem(last=False)
                del self.key_to_val_freq[lfu_key]  # Remove from main dictionary
            
            # Insert new key with frequency 1
            self.key_to_val_freq[key] = (value, 1)
            self.freq_to_nodes[1][key] = None
            self.min_freq = 1  # Reset min frequency to 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)