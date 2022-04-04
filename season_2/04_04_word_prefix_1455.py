class Solution(object):
    def isPrefixOfWord(self, sentence: str, searchWord: str):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        sentence = sentence.lower()
        searchWord = searchWord.lower()
        words = sentence.split()
        test_bits = map(lambda x: x.startswith(searchWord), words)
        i = test_bits.index(True) if True in test_bits else -2
        return i + 1