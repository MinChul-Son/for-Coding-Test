# # https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/882/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = dict()
        t_dict = dict()

        for i in s:
            if i in s_dict:
                s_dict[i] = s_dict.get(i) + 1
            else:
                s_dict[i] = 1
        for i in t:
            if i in t_dict:
                t_dict[i] = t_dict.get(i) + 1
            else:
                t_dict[i] = 1
        
        if s_dict == t_dict:
            return True
        else:
            return False

#--------------------------------------------------------------------------------

