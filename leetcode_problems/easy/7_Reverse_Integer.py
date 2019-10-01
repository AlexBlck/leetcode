class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            answer = int(str(x)[::-1])
        else:
            answer = int(str(x)[:0:-1]) * -1
        if abs(answer) > 2**31:
            answer = 0
        return answer

