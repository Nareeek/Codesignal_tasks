def growingPlant(upSpeed, downSpeed, desiredHeight):

    currentHeight = 0
    dayIndex = 1

    while currentHeight + upSpeed < desiredHeight:
        currentHeight += upSpeed - downSpeed
        dayIndex += 1

    return dayIndex