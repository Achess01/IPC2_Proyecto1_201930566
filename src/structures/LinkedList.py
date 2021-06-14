from ..structures.LLNode import LLNode


class LinkedList:
    def __init__(self):
        self.head = None
    
    def add(self, data):
        newNode = LLNode(data)
        if self.head == None:
            self.head = newNode
        else:
            aux = self.head
            while(aux.get_next() != None):
                aux = aux.get_next()
            aux.set_next(newNode)
    
    def get_node(self, index) -> LLNode:
        if self.head != None:
            counter = 1
            aux = self.head
            while aux != None:
                if counter == index:
                    return aux
                counter += 1
                aux = aux.get_next()
        return None
