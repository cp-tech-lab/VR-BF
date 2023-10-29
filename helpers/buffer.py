from typing import Any


class Buffer(list):

    def __init__(self, capacity: int):
        super().__init__([])
        self.capacity = capacity

    @property
    def full(self) -> bool:
        if len(self) == self.capacity:
            return True
        return False
    
    def append(self, o: Any):
        if not self.full:
            self += [o]


