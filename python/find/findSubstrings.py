class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.terminal = False
        # here we store the children nodes of this node
        # the letter of the children are the key, and the
        # TrieNode object is the value
        self.children = {}

def addFragmentToTrie(root, fragment):
    currentNode = root
    for letter in fragment:
        if letter not in currentNode.children:
            # create a new node
            currentNode.children[letter] = TrieNode(letter)
        currentNode = currentNode.children[letter]

    # we are at the final node. 
    # Mark it as terminal
    currentNode.terminal = True

def findSubstringInWord(w, root):
    lenLongSubstr, longestPos = 0,0

    for start_pos in range(len(w)):
        # reset to the beginning of the trie
        currNode = root

        for position in range(start_pos, len(w)):
            letter = w[position]
            if letter not in currNode.children:
                # we have run out of branches in trie,
                # so no use looking further down the string
                # from this starting position. Go back to
                # previous loop
                break
            currNode = currNode.children[letter]
            length = position - start_pos + 1
            if currNode.terminal and length > lenLongSubstr:
                lenLongSubstr = length
                longestPos   = start_pos

    # now we have found where the longest segment starts (longestPos)
    # and how long it is (longestSeenSubstring). 
    # We now have to place the square brackets
    if lenLongSubstr == 0:
        return w
    end = longestPos + lenLongSubstr
    return w[:longestPos] + "[" + w[longestPos: end] + "]" + w[end:]

# Not much to this function 
# It just ties everything else together
def findSubstrings(words, parts):
    # build the trie
    root = TrieNode('')
    for p in parts:
        addFragmentToTrie(root, p)
    return [findSubstringInWord(w, root) for w in words]