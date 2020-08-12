def telephoneGame(messages):
    answer = -1
    for i in range(1, len(messages)):
        if not messages[i] == messages[i - 1]:
            answer = i
            break
    return answer
