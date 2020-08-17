def splitAddress(address):
    pat = r"\w+"
    a = re.findall(pat, address)
    a.remove("com")
    
    return a