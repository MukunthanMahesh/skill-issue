class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        se = {}

        for n in range(len(nums)):
            diff = target - nums[n]
            if diff in se:
                return [se[diff], n]
            se[nums[n]] = n



        
