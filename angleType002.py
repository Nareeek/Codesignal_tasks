def angleType(measure):
    if measure == 90:
        return "right"
    if measure == 180:
        return "straight"
    
    if 0 < measure < 90:
        return "acute"
        
    return "obtuse" 