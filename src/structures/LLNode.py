class LLNode:
    def __init__(self, data): 
        self.data = data
        self.next = None

    def set_next(self, next):
        self.next = next
        
    def get_next(self) -> 'LLNode':
        return self.next
