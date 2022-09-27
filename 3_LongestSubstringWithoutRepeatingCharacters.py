"""
Given a string s, find the length of the longest substring without repeating characters.

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        current_sum = 0

        for starting_index in range(len(s)):
            # By default we need to add the first string to set
            collected_string = set(s[starting_index])
            current_sum = 1

            # Iteration of for loop starting from the next index
            for checking_index in range(starting_index + 1, len(s)):
                checking_char = s[checking_index]

                # Python set uses hash map which "in" operator's time complexity is in average O(1), but at worst O(n).
                # So, still worth using set rather than list
                if checking_char not in collected_string:
                    collected_string.add(checking_char)
                    current_sum += 1
                # if checking_char is in collected_string break for loop as we don't need to iterate more due to duplicated character in collected_string
                else:
                    break

            # After inner for loop has been fully iterated or "break" has been triggered, we should check whether we should update max_length
            if current_sum > max_length:
                max_length = current_sum

        return max_length


solution = Solution()

"""
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""
print(solution.lengthOfLongestSubstring(s="abcabcbb"))

# Input
# "jbpnbwwd"
# Output
# 5
# Expected
# 4

"""
Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
"""
print(solution.lengthOfLongestSubstring(s="bbbbb"))

"""
Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
print(solution.lengthOfLongestSubstring(s="pwwkew"))

print(solution.lengthOfLongestSubstring(s="jbpnbwwd"))  # Answer: 4
print(solution.lengthOfLongestSubstring(s="au"))  # Answer: 2
print(solution.lengthOfLongestSubstring(s=""))  # Answer: 0
print(solution.lengthOfLongestSubstring(s=" "))  # Answer: 1
