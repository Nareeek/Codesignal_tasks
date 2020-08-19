# 1
def isEarlier(time1, time2):
    return time1[0] < time2[0] or (time1[0]==time2[0] and time1[1]<time2[1])


# 2
def isEarlier(time1, time2):
    if time1[1] + 60 * time1[0] < time2[1] + 60 * time2[0]:
        return True
    return False