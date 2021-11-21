def higherVersion(ver1, ver2):
    version1 = ver1.split(".")
    version2 = ver2.split(".")

    for i in range(0,len(version1)):
        if int(version1[i])>int(version2[i]):
            return True
        elif int(version1[i])<int(version2[i]):
            return False
            
    return False