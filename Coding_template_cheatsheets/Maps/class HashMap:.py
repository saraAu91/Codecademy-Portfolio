class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for item in range(array_size)]

    def hash(self, key):
        self.key = key
        key_bytes = key.encode()
        #.encode() is a string method that converts a string into its corresponding bytes, a list-like object with the numerical representation of each character in the string.
        hash_code = sum(key_bytes)
        return hash_code
    
    def compressor(self, hash_code):
        return hash_code % self.array_size
    
    def assign(self, key, value):
        self.key = key
        self.value = value
        index = self.compressor(self.hash(key))
        self.array[index] = value
