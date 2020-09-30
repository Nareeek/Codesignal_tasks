def countSmallerToTheRight(nums):
    s = [0]
        
    for i in range(1, len(nums)):
        a = 0
        check = False
        
        if nums[i] < nums[i - 1]:
            a = s[i - 1] - 1
            check = True
            
        elif nums[i] == nums[i - 1]:
            a = s[i - 1]
            check = True
        
        if check == False:
            for j in range(i, len(nums)):
                if nums[i] > nums[j]:
                    a += 1
        
        s.append(a)
        check = False
        
    return sum(s)


a = [3, 8, 4, 1]
b = []
c = [-1]
d = [-1, -1]
e = [-1, -2]
f = [-1, 0]
g = [0, 2, 1]
h = [1, 0, 2]
i = [5, 3, 2, 4, 4, 35, 1, 14, 38, 35, 2]
j = [1, 2, 0]
k = [2, 0, 1]

print("a: 4 ->", countSmallerToTheRight(a))
print("b: 0 ->", countSmallerToTheRight(b))
print("c: 0 ->", countSmallerToTheRight(c))
print("d: 0 ->", countSmallerToTheRight(d))
print("e: 1 ->", countSmallerToTheRight(e))
print("f: 0 ->", countSmallerToTheRight(f))
print("j: 1 ->", countSmallerToTheRight(g))
print("g: 1 ->", countSmallerToTheRight(h))
print("i: 21 ->", countSmallerToTheRight(i))
print("j: 2 ->", countSmallerToTheRight(j))
print("k: 2 ->", countSmallerToTheRight(k))


