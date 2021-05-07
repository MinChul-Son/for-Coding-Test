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