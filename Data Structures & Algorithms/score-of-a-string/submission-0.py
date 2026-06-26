class Solution:
    def scoreOfString(self, s: str) -> int:
        sumo=0
        for i in range(len(s)-1):
            sumo+=abs(ord(s[i])-ord(s[i+1]))
        return sumo
        