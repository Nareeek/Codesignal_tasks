# 1
def videoPart(part, total):

    def getSeconds(time):
        h = int(time[0:2])
        m = int(time[3:5])
        s = int(time[6:8])
        return h * 60 * 60 + m * 60 + s

    def gcd(a, b):
        while a > 0:
            tmp = a
            a = b % a
            b = tmp
        return b

    partTime = getSeconds(part)
    totalTime = getSeconds(total)
    divisor = gcd(partTime, totalTime)
    return [partTime / divisor, totalTime / divisor]


# 2
import math

def videoPart(p, tot):
    p = [int(z) for z in p.split(':')]
    tot = [int(z) for z in tot.split(':')]
    dp = p[2]+p[1]*60+p[0]*3600
    dtot = tot[2]+tot[1]*60+tot[0]*3600 
    g = math.gcd(dp,dtot)
    return(dp//g,dtot//g)
