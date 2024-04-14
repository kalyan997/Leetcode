class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        dead_ends = set(deadends)
        sequence = [0,1,2,3,4,5,6,7,8,9]
        directions = ["1000", "0100", "0010", "0001","9000","0900","0090","0009"]
        #start_code = "0000"

        my_q = deque()
        visited = set()
        my_q.append(["0000",0])
        visited.add("0000")
        if "0000" in  dead_ends:
            return -1
        def add_strings(curr_node, directions):
            res_string = ""
            for i in range(0,4):
                res_string += str((int(curr_node[i])+int(direction[i]))%10)
            return res_string

        while my_q:
            curr_size = len(my_q)
            print(my_q)
            for i in range(curr_size):
                curr = my_q.popleft()
                curr_node, curr_level = curr[0], curr[1]

                if curr_node == target:
                    return curr_level
                for direction in directions:
                    next_code = add_strings(curr_node,direction)
                    if next_code not in visited and next_code not in dead_ends:
                        my_q.append([next_code, curr_level+1])
                        visited.add(next_code)
        return -1