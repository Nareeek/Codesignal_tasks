from collections import defaultdict

def swapLexOrder(strng, pairs):
    sets = find_connected_sets(pairs)
    char_order = {}
    for s in sets:
        char_order.update(get_char_locations(s, strng))

    largest = []
    for i in range(len(strng)):
        if i in char_order:
            largest.append(char_order[i])
        else:
            largest.append(strng[i])

    return ''.join(largest)

def find_connected_sets(pairs):
    connections = defaultdict(list)

    all_locs = set()
    for p in pairs:
        connections[p[0]].append(p[1])
        connections[p[1]].append(p[0])
        all_locs |= set(p)

    sets = []
    while len(all_locs) > 0:
        node = all_locs.pop()
        nodes = [node]
        s = {node}
        while len(nodes) > 0:
            key = nodes.pop()
            for n in connections[key]:
                if n not in s:
                    s.add(n)
                    all_locs.remove(n)
                    nodes.append(n)
        sets.append(s)
    return sets

    sets = []
    for p in pairs:
        pset = set(p)
        insert_jointed_set(sets, pset)
    return sets


def insert_jointed_set(sets, s):
    for st in sets:
        if not st.isdisjoint(s):
            st |= s
            return
    sets.append(s)

def get_char_locations(idx_set, strng):
    
    order = {}
    chars = []
    locs = [i-1 for i in idx_set]
    
    for i in locs:
        chars.append(strng[i])
    
    chars.sort(reverse=True)
    locs.sort()

    for i in range(len(locs)):
        order[locs[i]] = chars[i]
    return order


print(swapLexOrder("abdc", [[1,4],[3,4]]))