class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_dict = {}
        for c in s1:
            s1_dict[c] = s1_dict.get(c, 0) + 1


        substring_dict = {}
        left = 0
        right = left + len(s1) - 1

        for c in s2[left:right + 1]:
            substring_dict[c] = substring_dict.get(c, 0) + 1

        while True:  
            if s1_dict == substring_dict:
                return True
            
            if right == len(s2) - 1:
                return False  
            
            if substring_dict[s2[left]] == 1:
                del substring_dict[s2[left]]
            else: 
                substring_dict[s2[left]] -= 1
            
            left += 1

            right += 1
            substring_dict[s2[right]] = substring_dict.get(s2[right], 0) + 1