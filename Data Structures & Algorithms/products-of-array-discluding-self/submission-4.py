class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_products = []
        left_product = 1
        right_products = []
        right_product = 1
        for i in range(len(nums)):
            if i != 0:
                left_product *= nums[i-1]
                right_product *= nums[-i]
            left_products.append(left_product)
            right_products.append(right_product)

        right_products = right_products[::-1]

        products = []

        for i in range(len(nums)):
            products.append(left_products[i] * right_products[i])

        return products