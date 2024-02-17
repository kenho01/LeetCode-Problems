# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

# Thought Process:
# Append to the stack whenever we encounter '(', '[', '{'
# Check the last element on the stack when we encounter ')', ']', '}'
# Take note of cases where: 1. The string s is empty, 2. Stack is empty but s[i] reads ')', ']', '}'.

# Solution:

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        if len(s) <= 1:
            return False
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
            elif (s[i] == ")" or s[i] == "]" or s[i] == "}") and len(stack) == 0: 
                return False
            else:
                if s[i] == ")":
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        return False
                if s[i] == "]":
                    if stack[-1] == "[":
                        stack.pop()
                    else:
                        return False
                if s[i] == "}":
                    if stack[-1] == "{":
                        stack.pop()
                    else:
                        return False
        if len(stack) == 0:
            return True
        return False
                        


# Complexity Analysis:
    # Time Complexity: O(n)
    # Space Complexity: O(n)