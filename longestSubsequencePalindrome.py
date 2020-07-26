def longestSubsequencePalindrome(a):
    n = len(a)

    L = [[0 for x in range(n)] for x in range(n)] 

    for i in range(n):
        L[i][i] = 1

    for cl in range(2, n + 1): 
        for i in range(n + 1 - cl): 
            j = i + cl - 1
            
            if a[i] == a[j] and cl == 2: 
                L[i][j] = 2
                
            elif a[i] == a[j]: 
                L[i][j] = L[i + 1][j - 1] + 2
                
            else: 
                L[i][j] = max(L[i][j - 1], L[i + 1][j])

    return L[0][n - 1]


print(longestSubsequencePalindrome([1, 2, 4, 1]))