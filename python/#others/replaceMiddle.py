def replaceMiddle(arr):
    if len(arr) % 2 == 0:
        return arr[:len(arr) // 2 - 1] + [arr[len(arr) // 2] + arr[len(arr) // 2 - 1]] + arr[len(arr) // 2 + 1:]
    else:
        return arr