class Solution:
    def isValid(self, s: str) -> bool:

        opening_brackets = ["(", "[", "{"]
        closing_brackets = [")", "]", "}"]
        opens = []
        for i in s:
            if i in opening_brackets:
                opens.append(i)
            else:
                if len(opens) == 0:
                    return False
                
                prev_opening = opens.pop()
                match i:
                    case ")":
                        if prev_opening != "(":
                            return False
                    case "]":
                        if prev_opening != "[":
                            return False
                    case "}":
                        if prev_opening != "{":
                            return False
        
        if len(opens) != 0:
            return False
        
        return True
        