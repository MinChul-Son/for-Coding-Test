class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums1) > m:
            for _ in range(m, len(nums1)):
                del nums1[m]
            nums1 += nums2
            
        nums1.sort()
        