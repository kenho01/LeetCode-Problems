# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 

# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.

# Thought Process:
# Process the input string by removing whitespaces & special characters
# Convert all the characters in the resulting string into lowercase
# Use a 2 pointer approach (i, j) to traverse through the string until j < i

# Solution:

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleaned_s = ''.join(char for char in s if char.isalnum())
        cleaned_s_l = cleaned_s.lower()
        if len(cleaned_s_l) < 1:
            return True
        i = 0
        j = len(cleaned_s_l) - 1
        while (i < j):
            if cleaned_s_l[i] == cleaned_s_l[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

# Complexity Analysis:
#   Time Complexity: O(n)
#   Space Complexity: O(n)