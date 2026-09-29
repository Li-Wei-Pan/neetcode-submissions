class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        remaining_time = []
        cars = sorted(zip(position, speed), reverse = True) # (position, speed)
        for pos, spd in cars:
            remaining_time.append((target - pos)/spd)
        
        fleets = 0
        cur_head = 0
        result = [cur_head]
        for time in remaining_time:
            # if next one equals cur_head
            if time <= cur_head:
                continue
            # if slower
            else:
                fleets += 1
                cur_head = time
        return  fleets

