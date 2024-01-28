# 453. Minimum Moves to Equal Array Elements

#  Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

# In one move, you can increment n - 1 elements of the array by 1.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: 3
# Explanation: Only three moves are needed (remember each move increments two elements):
# [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
# Example 2:

# Input: nums = [1,1,1]
# Output: 0
 

# Constraints:

# n == nums.length
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
# The answer is guaranteed to fit in a 32-bit integer.


# Thought Process

# The equivalent of incrementing (n-1) elements by 1 is decrementing (n-1) elements
# by 1 until all elements in the array has the minimum value.

# Solution

class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        arr = set(nums)
        mini = min(nums)
        if len(arr) == 1:
            return count
        else:
            for i in range(len(nums)):
                if nums[i] > mini:
                    count += nums[i] - mini
                else:
                    pass
        return count
                
# Complexity Analysis
    # Time Complexity: O(n)
    # Space Complexity: O(n)
 