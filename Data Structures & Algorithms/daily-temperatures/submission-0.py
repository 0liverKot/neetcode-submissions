class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        max_stack = []

        for i in range(len(temperatures)):
            res.append(0)

            if len(max_stack) == 0:
                max_stack.append(temperatures[i])
                continue

            if max_stack[-1] >= temperatures[i]:
                max_stack.append(temperatures[i])

            if max_stack[-1] < temperatures[i]:
                max_stack.append(temperatures[i])
                for j in range(len(res) - 1, -1, -1):
                    if res[j] != 0:
                        continue
                    
                    if temperatures[j] < max_stack[-1]:
                        res[j] = i - j
        return res
                        
                         