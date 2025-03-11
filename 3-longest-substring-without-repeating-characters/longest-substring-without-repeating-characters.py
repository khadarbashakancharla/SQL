class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        max_len = 0
        sub = set()
        while right < len(s):
            if s[right] not in sub:
                sub.add(s[right])
                max_len = max(max_len,len(sub))
                right += 1
            else:
                sub.remove(s[left])
                left = left + 1
        return max_len        




        