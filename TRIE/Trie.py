from dataclasses import dataclass


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False


@dataclass
class Trie:
    def __init__(self):
        self.root = TrieNode()


def insert(trie, word):
        current = trie.root
        for ch in word:
            nextNode = current.children.get(ch)
            if not nextNode:
                nextNode = TrieNode()
                current.children.update({ch: nextNode})
            current = current.children.get(ch)
        current.endOfString = True
        print(f"string {word}, added successfully!")


def search(trie, word):
    current = trie.root
    for ch in word:
        nextNode = current.children.get(ch)
        if not nextNode:
            print(f"Word {word} not found")
            return
        current = nextNode
    if current.endOfString is True:
        print(f"Word {word} found")
    else:
        print(f"Word {word} not found")


def delete(trie, word, index):
    ch = word[index]
    current = trie.children.get(ch)
    toBeDeleted = False
    if len(current.children) > 1:
        delete(current, word, index + 1)
        return False
    if index == len(word) - 1:
        if len(current.children) >= 1:
            current.endOfString = False
            return False
        else:
            trie.children.pop(ch)
            return True
    if current.endOfString is True:
        delete(current, word, index + 1)
        return False
    toBeDeleted = delete(current, word, index + 1)
    if toBeDeleted is True:
        trie.children.pop(ch)
        return True
    else:
        return False


MyTrie = Trie()
insert(MyTrie, "Apple")
insert(MyTrie, "Api")
search(MyTrie, "Apple")
search(MyTrie, "Api")
# search(MyTrie, "bdd")
# search(MyTrie, "Apple")
# search(MyTrie, "Appl")
print(delete(MyTrie.root, "Api", 0))
search(MyTrie, "Api")
search(MyTrie, "Apple")
