import random

class RandomizedSet:

    def __init__(self):
        self.d = {}

    def insert(self, val: int) -> bool:
        # Check if the value is not already present in the dictionary
        if val not in self.d.keys():
            # Add the value to the dictionary with a placeholder value
            self.d[val] = 1
            return True
        return False

    def remove(self, val: int) -> bool:
        # Check if the value exists in the dictionary
        if val in self.d.keys():
            # Remove the value from the dictionary
            self.d.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        # Select a random key from the dictionary
        random_num = random.choice(list(self.d.keys()))
        return random_num