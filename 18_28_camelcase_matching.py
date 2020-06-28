class trieNode():
    def __init__(self):
        self.end_pattern = None
        self.children = {}
        return
    
    def insert(self, pattern, whole_pattern):
        if pattern == "":
            self.end_pattern = whole_pattern
            return

        char = pattern[0]

        if char not in self.children:
            self.children[char] = trieNode()
        
        return self.children[char].insert(pattern[1::], whole_pattern)


def bank_appender(root, bank):
    if root.end_pattern:
        bank.append(root.end_pattern)

    for child in root.children:
        if child.islower():
            bank_appender(root.children[child], bank)
    
    return
    
# recommended australian beers
# evalprase: VB
# evalprase: Stone & Wood
# evalprase: Coopers
# also furphy
def validate_against_pattern(root, pattern, bank):
    
    if pattern == "":
        bank_appender(root, bank)
        return


    char = pattern[0]
    for child in root.children:
        if child.isupper() and child != char:
            continue
        else:
            upcoming_pattern = pattern
            if child == char:
                upcoming_pattern = pattern[1::]
            node = root.children[child]
            validate_against_pattern(node, upcoming_pattern, bank)
    return
        

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        root = trieNode()

        for q in queries:
            root.insert(q, q)
        
        bank = []
        validate_against_pattern(root, pattern, bank)

        return [x in bank for x in queries]