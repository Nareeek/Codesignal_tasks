from itertools import combinations as comb


def longestSubsequencePalindrome(a):
    if len(a) == len(set(a)):
        return 1
        
    seq = []
    for i in range(1, len(a) + 1):
        seq.extend(list(comb(a, i)))
    
#     t = max(map(check, seq))
    
#     return t
        
# def check(sub):
#     l = len(sub)
#     first = 0
#     last = l - 1 
       
#     while first < last:
#         if sub[first] == sub[last]:
#             first += 1
#             last -= 1
#         else:
#             return 0
            
#     return l