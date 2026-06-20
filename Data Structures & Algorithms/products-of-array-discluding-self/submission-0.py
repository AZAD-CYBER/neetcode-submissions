class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize result array with 1s
        result = [1] * len(nums)

        # First pass: store product of all elements to the LEFT of each index
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        # Second pass: multiply by product of all elements to the RIGHT
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result
