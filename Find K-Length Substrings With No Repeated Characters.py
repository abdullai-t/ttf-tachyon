def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        count = 0 
        if k> len(s) -1:
            return count
        for index in range(len(s)+1): # O(n)
            sub_str = s[index:k+index]
            if len(set(sub_str)) ==k: #O(1)
                count+=1
        return count
