# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        candidacy_list = [[x, rand7()] for x in range(1,11)]

        while len(candidacy_list) > 1:
            candidacy_list.sort(key=lambda x: x[1])
            i = 0
            lowscore = candidacy_list[0][1]
            while i < len(candidacy_list) and candidacy_list[i][1] == lowscore:
                candidacy_list[i][1] = rand7()
                i += 1

            candidacy_list = candidacy_list[0:i]

        return candidacy_list[0][0]