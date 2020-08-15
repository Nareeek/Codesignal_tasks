# 1
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

# 2
def longestSubsequencePalindrome(a):
    n = len(a)       
    dp = [[0 for j in range(n)] for i in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for i in range(1, n):
        if a[i - 1] == a[i]:
            dp[i - 1][i] = 2
        else:
            dp[i - 1][i] = 1

    for L in range(3, n + 1):
        for pos in range(1, (n - L + 1) + 1):
            i = pos - 1
            j = i + L - 1
            if a[i] == a[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
                
    return dp[0][n - 1]
    
    

print(longestSubsequencePalindrome([1, 2, 4, 1]))

