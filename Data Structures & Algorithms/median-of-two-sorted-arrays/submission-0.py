class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        l, r = 0, len(nums) - 1
        m = ((l + r) // 2, -(-(l + r) // 2))
        print(m)
        if m[0] == m[1]:
            return nums[m[0]]
        else:
            return (nums[m[0]] + nums[m[1]]) / 2
