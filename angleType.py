# 1
def angleType(measure):
    if measure < 90:
        return "acute"
    if measure == 90:
        return "right"
    if 90 < measure < 180:
        return "obtuse"
    if measure == 180:
        return "straight"
    
# 2
def angleType(measure):
    if measure == 90:
        return "right"
    if measure == 180:
        return "straight"
    
    if 0 < measure < 90:
        return "acute"
        
    return "obtuse" 