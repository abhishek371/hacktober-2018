class stack:
    def __init__(self,size):
        self.top = -1 
        self.A = [None for i in range(size)]
        self.max = size

    def push(self,x):
        if self.top > self.max:
            return None 
        self.top = self.top + 1 
        self.A[self.top] = x
        return True 

    def pop(self):
        if self.top < 0 :
            return None 
        r = self.A[self.top]
        self.top = self.top - 1 
        return r 

    def isEmpty(self):
        if self.top < 0 :
            return True 
        return False 

    def peek(self):
        if self.top >= 0 and self.top < self.max:
            return self.A[self.top]
        return None 

def main():
    S = stack(100)
    print(S.pop())
    S.push(9)
    S.push(8)
    S.push(-76)
    print(S.peek())
    print(S.pop(),S.pop())

if __name__ == '__main__':
    main() 

        

