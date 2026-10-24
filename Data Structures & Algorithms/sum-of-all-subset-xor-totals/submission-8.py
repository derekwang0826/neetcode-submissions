class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(index, cur_xor):
            if index == len(nums):
                return cur_xor
            return dfs(index + 1, cur_xor ^ nums[index]) + dfs(index + 1, cur_xor)
        return dfs(0, 0)