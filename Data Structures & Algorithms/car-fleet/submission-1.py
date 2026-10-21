class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        map = {}
        for i in range(len(position)):
            map[position[i]] = speed[i]

        position.sort(reverse=True)

        res = 1
        fleet_time = []
        for i in range(len(position)):
            time = (target - position[i]) / map[position[i]]

            if len(fleet_time) == 0:
                fleet_time.append(time)
            
            elif fleet_time[0] >= time:
                fleet_time.append(time)
            
            else:
                res += 1
                fleet_time = [time]

        return res 

