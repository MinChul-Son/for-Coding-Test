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
