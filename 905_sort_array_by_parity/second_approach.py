class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odds = []
        counter = 0
        while counter < len(A):
            if A[counter]%2 != 0:
                odds.append(A.pop(counter))
            else:
                counter += 1
        return A + odds
