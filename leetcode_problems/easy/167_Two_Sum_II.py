class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a = 0
        b = -1
        while True: # Solution guaranteed in problem description
            if numbers[a] + numbers[b] == target:
                return [a+1, len(numbers)+b+1]
            elif numbers[a] + numbers[b] < target:
                a += 1
            else:
                b -= 1
