from typing import List

class Node:
    def __init__(self, letter: str):
        self.letter = letter
        self.children = []

    letter = ''
    children = []

def add_to_trie(root: Node, word):

    for child in root.children:
        if child.letter == word[0]:
            if len(word) == 1:
                return True
            else:
                del word[0]
                return add_to_trie(child, word)
    
    if len(word) == 1:
        root.children.append(Node(word[0]))
        return True
    else:
        return False

    return

# def print_trie(root):
#     print((root.letter, [x.letter for x in root.children]))
#     for child in root.children:
#         print_trie(child)
#     return

class Solution:
    def longestWord(self, words: List[str]) -> str:
        if len(words) == 0:
            return ''
        
        if min([len(x) for x in words]) > 1:
            return ''
        
        words.sort()
        words.sort(key= lambda x: len(x))

        best_word = ''
        root = Node('')
        last_len = 0
        cur_len = 0
        for word in words:
            cur_len = len(word)
            if cur_len > last_len + 1:
                return best_word
            
            lword = list(word)
            added = add_to_trie(root, lword)
            # print_trie(root)
            if added:
                if len(word) > len(best_word):
                    best_word = word
            
            last_len = cur_len
        
        return best_word