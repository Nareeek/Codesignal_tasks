def baseConversion(n, x):
    return (str(hex(int(str(n),x))[2:]))


print(baseConversion("1302", 5))