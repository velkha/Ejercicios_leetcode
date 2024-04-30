class MinStack(object):
    #Logico pero mas lento (no se guardan datos de mas)
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        if(item is not None):
            self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return 0

    def top(self):
        if not self.is_empty():
            return self.items[-1]
        return 0

    def getMin(self):
        if not self.is_empty():
            return min(self.items)
        return 0 
    
    
    
    
    """
    RAPIDO PERO NO LOGICO (GUARDAMOS DATOS DE MAS PARA NO HACER MUCHAS OPERACIONES EN EL CASO ESPECIFICO DEL EJERCICIO)
    def __init__(self):
        # Initialize the stack to hold tuples of (element, current_min)
        self.stack = []

    def push(self, val):
        if not self.stack:
            self.stack.append((val, val))
        else:
            current_min = min(val, self.stack[-1][1])
            self.stack.append((val, current_min))

    def pop(self):
        if self.stack:
            self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1][0]
        return None

    def getMin(self):
        if self.stack:
            return self.stack[-1][1]
        return None
    """
