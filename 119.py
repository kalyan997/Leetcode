class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascals_triangle = []
        prev_row = []
        numRows = rowIndex+1
        for i in range(numRows):
            curr_row = []
            for j in range(1,i+2):
                if j == 1 or j ==i+1:
                    curr_row.append(1)
                else:
                    curr_row.append(prev_row[j-2]+prev_row[j-1])
            prev_row = curr_row
            pascals_triangle.append(curr_row)

        return pascals_triangle[rowIndex]