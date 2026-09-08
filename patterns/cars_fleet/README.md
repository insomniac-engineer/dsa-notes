Link: [853. Car Fleet](../../problems/0853-car-fleet/)

```python3
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars_sorted = sorted(zip(position, speed), reverse = True)
        max_time = 0
        fleets = 0
        for pos, speed in cars_sorted:
            time = (target - pos)/speed
            if time > max_time:
                fleets += 1
                max_time = time
        return fleets
```

I don't really consider this task as stack one, although on LC it's marked as stack problem.

The main idea is that NEW fleet is formed only when time left for the current car is MORE than maximum one. Else, the cars will be stacked (same fleet) or the road would be clear.

See this drawing:
![Cars Fleet](patterns/cars_fleet/cars_fleet_draw.png)
