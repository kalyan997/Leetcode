class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        my_stack = []
        next_greater_element = [-1]*n
        res = 0
        for i, h in enumerate(height):
            while my_stack and my_stack[-1][0] <= h:
                curr_ind, curr_height = my_stack[-1][1], my_stack[-1][0]
                my_stack.pop()
                if not my_stack:
                    break
                next_greater_element[curr_ind] = h
                bounded_h = min(h,my_stack[-1][0])-curr_height
                dist = i-my_stack[-1][1]-1
                res += bounded_h*dist
                
            my_stack.append([h,i])
        
        print(next_greater_element)
        return res
        