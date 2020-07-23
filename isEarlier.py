def isEarlier(time1, time2):
    return time1[0] < time2[0] or (time1[0]==time2[0] and time1[1]<time2[1])