def validTime(time):
    hour = int(time[:2])
    minute = int(time[3:])
    return hour < 24 and minute < 60