class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)

        seen = set()

        res = 0

        left = 0
        right = 1
        
        while True:
            if right > len(s) - 1:
                break

            if s[left] not in seen:
                seen.add(s[left])

            if s[right] in seen:
                while s[left] != s[right]:
                    seen.remove(s[left])
                    left += 1
                left += 1
            else: 
                seen.add(s[right])
            
            if right - left + 1 > res:
                res = right - left + 1
            
            right += 1

        return res
                    
        