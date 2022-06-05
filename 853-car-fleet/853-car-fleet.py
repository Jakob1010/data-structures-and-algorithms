class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_and_speed = []
        fleet_cnt = 0
        
        for p, s in zip(position,speed):
            position_and_speed.append([p,s])
            
        position_and_speed.sort(key=lambda x: x[0])
        last_finish_time = -1
        
        while position_and_speed:
            p, s = position_and_speed.pop()
            remaining_positions = target-p
            finish_time = (remaining_positions) / s
            
            if finish_time > last_finish_time:
                last_finish_time = finish_time
                fleet_cnt += 1
            
        return fleet_cnt
        