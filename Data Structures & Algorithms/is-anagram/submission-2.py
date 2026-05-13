class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm1, hm2 = {}, {}
        for c1 in s:
            hm1[c1] = hm1.get(c1, 0) + 1
        for c2 in t:
            hm2[c2] = hm2.get(c2, 0) + 1
        return hm1 == hm2
