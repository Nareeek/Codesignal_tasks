# 1
def numberOfTriangles2(sticks):
    cnt = 0
    sticks = sorted(sticks,reverse = True)
    for i in range(len(sticks)):
        for j in range(i+1,len(sticks)):
            for k in range(j+1,len(sticks)):
                if sticks[k]+sticks[j]>sticks[i]:
                    cnt += 1

    return cnt

# 2
def numberOfTriangles2(s):
    out = 0
    for i in range(0,len(s)-2):
        for j in range(i+1,len(s)-1):
            for k in range(j+1,len(s)):
                if s[k]<s[i]+s[j]:
                    print(s[i],s[j],s[k])
                    out+=1
    return out

print(numberOfTriangles2([3, 5, 7, 9])) # == 3

