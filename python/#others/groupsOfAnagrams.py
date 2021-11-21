def groupsOfAnagrams(words):
    s = set()
    for w in words:
        s.add( ''.join( sorted( w)))
    return len(s)


print(groupsOfAnagrams(["tea", 
 "eat", 
 "apple", 
 "ate", 
 "vaja", 
 "cut", 
 "java", 
 "utc"]))