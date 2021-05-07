# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/727/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0: return 0
        
        
        i=0 
        for j in range(1,len(nums)):
            if nums[i]!=nums[j]: # If not duplicated
                i+=1  # Move i
                nums[i]=nums[j] # Swap
        
        return i+1

#----------------------------------------------------------------------------------------------------
# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/564/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == sorted(prices, reverse=True):
            return 0
        total_prices = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                total_prices += prices[i+1] - prices[i]
        return total_prices



#---------------------------------------------------------------------------------------------------
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == len(set(nums)):
            return False
        return True
        


#-------------------------------------------------------------------------------------------------
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        current_num = nums[0]
        check_single = 1
        for i in range(1, len(nums)):
            if nums[i] != current_num:
                if check_single == 1:
                    return current_num
                check_single = 1
                current_num = nums[i]
            else:
                check_single += 1
        return current_num
            

#---------------------------------------------------------------------------------------------------
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        if len(nums1) < len(nums2):
            for i in nums1:
                if i in nums2:
                    answer.append(i)
                    nums2.remove(i)
        else:
            for i in nums2:
                if i in nums1:
                    answer.append(i)
                    nums1.remove(i)
        return answer
        


