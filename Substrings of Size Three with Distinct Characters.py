class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        goods = 0
        k = 3
        for x in range(len(s)+1):
          m = set(s[x:x+k])
          if len(m)==k:
              goods+=1

        return goods
