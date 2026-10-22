class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        largest = 0
        for pile in piles:
            if pile > largest:
                largest = pile

        left, right = 1, largest
        res = None

        while left <= right:
            rate = left + (right - left) // 2
            sum_time = 0
            for pile in piles:
                if pile % rate != 0:
                    sum_time += (pile // rate) + 1
                else: 
                    sum_time += pile // rate

            if sum_time <= h:
                if res is None or rate < res:
                    res = rate
                right = rate - 1
            
            if sum_time > h:
                left = rate + 1

        return res




