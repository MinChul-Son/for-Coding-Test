# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/885/
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1

#--------------------------------------------------------------------------
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/887/
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs, key=lambda x: len(x))
        end = 0
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if strs[j][i] == strs[0][i]:
                    pass
                else:
                    break
            else:
                end += 1
                continue
            break
        return strs[0][0:end]
