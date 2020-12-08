def domainType(domains):
    
    descriptions = []
    
    for domain in domains:
        if domain.endswith(".com"):
            descriptions.append("commercial")
        elif domain.endswith(".net"):
            descriptions.append("network") 
        elif domain.endswith(".org"):
            descriptions.append("organization")
        elif domain.endswith(".info"):
            descriptions.append("information") 
            
    return descriptions