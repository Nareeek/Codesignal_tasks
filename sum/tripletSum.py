def tripletSum(x, a):
    a.sort()
    for i in range(len(a) - 2):
        left = i + 1
        right = len(a) - 1
        
        while left < right:
            result = a[i] + a[left] + a[right]
            if result == x:
                print(a[i], " ", a[left], " ", a[right])
                return True
            elif result < x:
                left += 1
            elif result >= x:
                right -= 1
    return False
            