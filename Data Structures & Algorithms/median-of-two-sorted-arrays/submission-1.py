class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        n = len(nums)
        m = ((n - 1) // 2, n // 2)

        if m[0] == m[1]:
            return nums[m[0]]
        else:
            return (nums[m[0]] + nums[m[1]]) / 2
