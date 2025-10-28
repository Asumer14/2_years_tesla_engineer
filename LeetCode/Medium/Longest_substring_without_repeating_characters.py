class Solution(object):
    def lengthOfLongestSubstring(self, s):
      char_index = {}
      # write down the position where string last shown up.
      left = 0
      ans = 0   

      for right in range(len(s)):
        current_char = s[right]

        # if the string already exist in the window, move the left
        if current_char in char_index and char_index[current_char] >= left:
          left = char_index[current_char] + 1

        # update the position of string
        char_index[current_char] = right

        # update the answer
        ans = max(ans, right - left + 1)

      return ans