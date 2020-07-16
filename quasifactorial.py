def quasifactorial(n):
    answer = 1
    for i in range(2, n+1):
        answer *= i
        answer -= 1
    return answer

print(quasifactorial(8))