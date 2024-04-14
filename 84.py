class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        my_stack = []

        max_area = 0

        for curr_ind, curr_hei in enumerate(heights):
            start = curr_ind
            while my_stack and curr_hei<my_stack[-1][0]:
                prev = my_stack.pop()
                prev_hei, prev_ind = prev[0], prev[1]
                curr_area = prev_hei* (curr_ind-prev_ind)
                max_area = max(curr_area,max_area)
                start = prev_ind
            my_stack.append([curr_hei,start])

        while my_stack:
            prev = my_stack.pop()
            prev_hei, prev_ind = prev[0], prev[1]
            curr_area = prev_hei* (n-prev_ind)
            max_area = max(curr_area,max_area)
        return max_area