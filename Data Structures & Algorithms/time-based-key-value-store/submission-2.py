class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        curr = self.map.get(key, [])
        curr.append((value, timestamp))
        self.map[key] = curr

    def get(self, key: str, timestamp: int) -> str:
        values = self.map.get(key, None)
        if values is None:
            return "" 

        curr = ""

        left = 0
        right = len(values) - 1
        
        while left <= right:
            mid = left + (right - left) // 2

            if values[mid][1] == timestamp:
                return values[mid][0]
            
            if values[mid][1] > timestamp:
                right = mid - 1
            else: 
                curr = values[mid][0]
                left = mid + 1

        return curr
