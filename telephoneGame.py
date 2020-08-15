def telephoneGame(messages):
    answer = -1
    for i in range(1, len(messages)):
        if not messages[i] == messages[i - 1]:
            answer = i
            break
    return answer


# 2

def telephoneGame(messages):
    prev = messages[0]
    for i, m in enumerate(messages[1:]):
        if m != prev: return i + 1
    return -1

# 3
def telephoneGame(messages):
    answer = -1
    for i in range(1, len(messages)):
        if messages[i] != messages[i - 1]:
            answer = i
            break
    return answer