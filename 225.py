class MyStack:

    def __init__(self):
        self.q_1 = deque()
        self.q_2 = deque()
        
    def push(self, x: int) -> None:
        self.q_1.append(x)
        while len(self.q_1)>1:
            curr_ele = self.q_1.popleft()
            self.q_2.append(curr_ele)
        while len(self.q_2)>0:
            curr_ele = self.q_2.popleft()
            self.q_1.append(curr_ele)

    def pop(self) -> int:
        return self.q_1.popleft()
        

    def top(self) -> int:
        return self.q_1[0]

    def empty(self) -> bool:
        if len(self.q_1)==0:
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()