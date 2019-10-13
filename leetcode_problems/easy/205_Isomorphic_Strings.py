class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ss = {}
        tt = {}
        for i, (letter_s, letter_t) in enumerate(zip(s, t)):
            if letter_s in ss.keys():
                ss[letter_s].append(i)
            else:
                ss[letter_s] = [i]
                
            if letter_t in tt.keys():
                tt[letter_t].append(i)
            else:
                tt[letter_t] = [i]
                
        
        return list(ss.values()) == list(tt.values())
