class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        left,right = 0,len(numbers)-1
        while left<right:
            two_sum = numbers[left]+numbers[right]
            if two_sum>target:
                right -= 1
            elif two_sum<target:
                left+=1
            else:
                res.append(left+1)
                res.append(right+1)
                left +=1
                right -= 1
                while left<right and numbers[left]==numbers[left-1]:
                    left += 1
        return res