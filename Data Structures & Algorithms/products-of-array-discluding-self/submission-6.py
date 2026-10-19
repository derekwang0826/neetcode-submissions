class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        product = 1
        right_product = 1
        for i in range(len(nums)):
            if i != 0:
                product *= nums[i-1]
            products.append(product)

        for j in range(len(nums) - 1, -1, -1):
            if j != len(nums) - 1:
                right_product *= nums[j + 1]
            products[j] *= right_product
        
        return products