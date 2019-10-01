class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        ans = []
        compare = x if (x < y or y == 1) and x != 1 else y
        max_power = 0
        while compare**max_power < bound:
            if x == 1 and y == 1:
                compare = 2
            max_power += 1
        for i in range(max_power):
            for j in range(max_power):
                v = x**i + y**j
                if v <= bound and not v in ans:
                    ans.append(v)
        return ans
