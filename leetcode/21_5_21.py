# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/879/
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        

#-------------------------------------------------------------------------------------------
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/880/
class Solution:
    def reverse(self, x: int) -> int:
        x = list(str(x))
        x.reverse()
        if x[-1] == '-':
            x = int('-' + "".join(x[0:-1]))
        else:
            x = int("".join(x))
        max_num = 2**31
        if x > max_num or x < -max_num:
            return 0
        
        return x
        

#--------------------------------------------------------------------------------------------
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/881/
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i, p in enumerate(s):
            if s.count(p) == 1:
                return i
        else:
            return -1