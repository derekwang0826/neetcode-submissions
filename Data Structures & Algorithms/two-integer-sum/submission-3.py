class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = [target - i for i in nums]
        for idx, i in enumerate(complements):
            if i in nums:
                if i == nums[idx]:
                    if nums.count(i) > 1:
                        first = nums.index(i)
                        second = nums.index(i, first + 1)
                        return [first, second]
                    continue
                answer = [idx, nums.index(i)]
                return sorted(answer)