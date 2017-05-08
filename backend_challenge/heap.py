class Heap():
    
    def __init__(self, comparator = lambda a, b: a > b):
        self.data = []
        self.compare = comparator
    
    def insert(self, e):
        self.data.append(e)
        self.bubble_up()
    
    def remove_top(self):
        if len(self.data) == 0:
            return self.data.pop()
        else:
            top = self.data[0]
            self.data[0] = self.data.pop()
            self.bubble_down()
            return top
    
    def bubble_up(self):
        i = len(self.data) - 1
        A = self.data
        while i > 0:
            if self.compare(A[i], A[i // 2]) > 0:
                A[i], A[i // 2] = A[i // 2], A[i]
            i = i // 2
    
    def bubble_down(self):
        i = 0
        while i is not None:
            i = self.bubble_with_child(i)
                      
    def bubble_with_child(self, i):
        last = len(self.data) - 1
        
        if i * 2 + 1 > last: # no children
            return None
        
        A = self.data
        left = A[i * 2 + 1]
        
        if i * 2 + 2 <= last:
            right = A[i * 2 + 2]
            # swap with appropriate child, depending on comparator function
            appr_child = 2 * i + 1 if self.compare(right, left) < 0 else 2 * i + 2
            if self.compare(A[i], A[appr_child]) < 0:
                A[i], A[appr_child] = A[appr_child], A[i]
                return appr_child
        else:
            # swap with left child if necessary
            if self.compare(A[i], left) < 0:
                A[i], A[i * 2] = A[i * 2], A[i]
                return 2 * i + 1
        return None

    def size(self):
        return len(self.data)
    
    def peek(self):
        return self.data[0]
    
if __name__ == '__main__':
    h = Heap(lambda x, y : x > y)
    
    h.insert(2)
    print(h.data)
    
    h.insert(3)
    print(h.data)
    
    h.insert(1)
    print(h.data)
    
    h.insert(0.1)
    print(h.data)
    
    h.insert(7)
    print(h.data)
    
    h.insert(5)
    print(h.data)
    
    h.insert(4)
    print(h.data)