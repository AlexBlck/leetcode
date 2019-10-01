class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        alice_total = sum(A)
        bob_total = sum(B)
        d = alice_total - bob_total
        A = set(A)
        B = set(B)
        if d > 0:
            for a in A:
                if a >= (d//2 + 1) and a - d//2 in B:
                    return [a, a - d//2]
        else:
            for b in B:
                if b >= (abs(d)//2 + 1) and d//2 + b in A:
                    return [d//2 + b, b]

