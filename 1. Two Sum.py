class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return 0, 1
        else:
            for i in range(len(nums)):
                tmp = target - nums[i]
                if tmp in nums[i+1:]:
                    return i, nums[i+1:].index(tmp)+i+1