class Stack():
    def __init__(self) -> None:
        self._data = []

    def push(self,element):
        self._data.append(element)
        print("Element {} Pushed Successfully".format(element))

    def isEmpty(self):
        if len(self._data) == 0:
            return True
        return False
    
    def pop(self):
        if self.isEmpty():
            print("Stack is empty!")
        else:
            return self._data.pop()
        
    def top(self):
        if self.isEmpty():
            print("Stack is empty!")
            return -1
        else:
            return self._data[-1]
    

st = Stack()

st.push(1)
print(st.pop())
print(st.top())
        

