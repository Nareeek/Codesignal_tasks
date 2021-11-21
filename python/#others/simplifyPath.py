# 1
def simplifyPath(path):
    st = ['/']
    path = path.split("/")
    for i in path:
        if i == '..':
            if len(st) > 1:
                st.pop()
            else:
                continue
        elif i == '.':
            continue
        elif i != '':
            st.append("/" + str(i))
    if len(st) == 1:
        return "/"
    return "".join(st[1:])


# 2
import os
def simplifyPath(path):
    return os.path.realpath( path )


# 3
def simplifyPath(path):

    stack = [x for x in reversed(path.split(sep='/'))]

    output = []
    while stack:
        k = stack.pop()
        if k in ['', '.'] : pass
        elif k == '..':
            try:
                output.pop()
                output.pop()
            except:
                pass
        else:
            output.append(k)
            output.append('/')
    try:
        output.pop()
    except:
        pass

    return(''.join(['/'] + output))


