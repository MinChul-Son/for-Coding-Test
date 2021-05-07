# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        plus_one = str(int("".join(list(map(str, digits)))) + 1)
        digits = []
        for i in plus_one:
            digits.append(int(i))
        return digits


#-------------------------------------------------------------------------------------------
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/567/
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            pass
        else:
            count_zero = nums.count(0)
            for _ in range(count_zero):
                nums.remove(0)
                nums.append(0)


#---------------------------------------------------------------------------------------------
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/546/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        for i,p in enumerate(nums):
            if (target-p) in nums[i+1:]:
                answer.append(i)
                answer.append(i + nums[i+1:].index(target-p) + 1)
        return answer


#-----------------------------------------------------------------------------------------------
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/770/
import copy
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        ret = copy.deepcopy(matrix)

        for r in range(N):
            for c in range(N):
                matrix[c][N-1-r] = ret[r][c]