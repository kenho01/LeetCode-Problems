# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

# Thought Process:

# Solution:
# Initialize a hashmap to track the count of each character on string s
# Use the same hashmap to decrement the count of each character on string t
# If the anagram is valid, the resulting values in the hashmap would be 0s. Else, it is invalid.

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count = [0 for i in range(26)]
        for i in s:
            count[ord(i) - 97] += 1
        print(count)
        for j in t:
            count[ord(j) - 97] -= 1
        for k in count:
            if k != 0:
                return False
        return True
        
# Complexity Analysis
#   Time Complexity: O(n)
#   Space Complexity: O(n)