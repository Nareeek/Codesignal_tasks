def differentRightmostBit(n, m):
    
    return 2 ** [i for i in range(len(bin(n)[2:].zfill((-len(bin(n)[2:])) % 8 + len(bin(n)[2:])))) if bin(n)[2:].zfill((-len(bin(n)[2:])) % 8 + len(bin(n)[2:]))[::-1][i] != bin(m)[2:].zfill((-len(bin(m)[2:])) % 8 + len(bin(m)[2:]))[::-1][i]][0]
    
    List = []

    for i in range(len(bin(n)[2:].zfill((-len(bin(n)[2:])) % 8 + len(bin(n)[2:])))):
        if bin(n)[2:].zfill((-len(bin(n)[2:])) % 8 + len(bin(n)[2:]))[::-1][i] != bin(m)[2:].zfill((-len(bin(m)[2:])) % 8 + len(bin(m)[2:]))[::-1][i]:
            List.append(i)
            return List[0]      
        
        

print(differentRightmostBit(1073741823, 1071513599))