# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        plus_one = str(int("".join(list(map(str, digits)))) + 1)
        digits = []
        for i in plus_one:
            digits.append(int(i))
        return digits