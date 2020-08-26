import math
def videoPart(p, tot):
    p = [int(z) for z in p.split(':')]
    tot = [int(z) for z in tot.split(':')]
    dp = p[2]+p[1]*60+p[0]*3600
    dtot = tot[2]+tot[1]*60+tot[0]*3600 
    g = math.gcd(dp,dtot)
    return(dp//g,dtot//g)
