import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0 
        end = len(s) - 1

        alphanumeric = list(string.ascii_lowercase + string.ascii_uppercase + string.digits) 

        for i in range(int(len(s) / 2)):
            while s[start] not in alphanumeric:
                start += 1
                if start == len(s) - 1:
                    return True

            while s[end] not in alphanumeric:
                end -= 1
                if end == 0:
                    return True    
        
            if s[start].lower() != s[end].lower():
                return False

            start += 1
            end -= 1

        return True
        