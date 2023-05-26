class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        k_beaty = 0
        num_str = str(num)
        for n in range(len(num_str)+1):
            sub_num = num_str[n:k+n]
            if sub_num and len(sub_num)== k and int(sub_num) !=0:
                if num % int(sub_num) == 0:
                     k_beaty +=1
        return k_beaty
