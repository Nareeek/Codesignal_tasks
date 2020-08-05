arr = ["at", "and", "an", "add", "bat"]

def search(word):
    flag = False
    if word in arr:
        return True
    for x in arr:
        if len(x) == len(word):
            for i in range(len(x)):
                if word[i] != ".":
                    if x[i] != word[i]:
                        break
                if i == len(x) - 1:
                    flag = True
            
            
    return flag

print(search(".at"))