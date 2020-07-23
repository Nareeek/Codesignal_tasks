 def waterTubes(water, flowPerMinute):
    result = 0

    for i in range(len(water)):
        minutes = water[i] // flowPerMinute[i]
        if water[i] % flowPerMinute[i]:
            minutes += 1

        if result < minutes:
            result = minutes
    return result