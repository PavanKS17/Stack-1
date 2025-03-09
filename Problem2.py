# In this approach, we traverse the array twice looking for next element greater than the current element.
# We use a stack to store the index of the elements in the array.
# If the current element is greater than the top of the stack, we pop from the stack and update the result array.
# TC: O(n)
# SC: O(n)


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n
        stack = []
        for i in range(2 * n):
            while stack and nums[i % n] > nums[stack[-1]]:
                popped = stack.pop()
                result[popped] = nums[i % n]
            if i < n:
                stack.append(i)
            
        return result