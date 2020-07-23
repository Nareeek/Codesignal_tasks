def variableName(name):
    if name[0].isdigit():
        return False
        
    for a in name:
        if not ( a.isalpha() or a.isdigit() or a == '_' ):
            return False
    return True