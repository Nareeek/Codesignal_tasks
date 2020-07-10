def lineUp(commands):
    if len(commands) == 1:
        if commands[0] in ["L", "R"]:
            return 0
        else:
            return 1

    nar = ["RR", "LL", "LR", "RL"]

    flag = True
    count = 0

    i = 0
    while i <= len(commands) - 2:

        if flag:
            if commands[i: i + 2] in nar:
                i += 2;
                flag = True;
                count += 1

            elif commands[i] == "A":
                i += 1;
                flag = True;
                count += 1

            else:
                flag = False;
                i += 1

            if commands[i] == "A" and i == len(commands) - 1:
                count += 1



        elif (flag == False) and commands[i] == "A":
            if commands[-1] != "A" and i == len(commands) - 2:
                count += 1
            i += 1

        elif (flag == True) and commands[i] in ["L", "R"]:
            flag = False;
            i += 1

        elif (flag == False) and commands[i] in ["L", "R"]:
            flag = True;
            count += 1;
            i += 1

    return count


print(lineUp("LALRRLRLRA"))
