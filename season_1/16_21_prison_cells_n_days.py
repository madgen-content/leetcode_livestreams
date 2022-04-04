# easy but bad soln, reallocates list per step
def advance_prison(start):
    finish = start[::]

    for i in range(len(start)):
        if i == 0 or i == len(start)-1:
            finish[i] = 0
        else:
            left = start[i-1]
            right = start[i+1]
            finish[i] = int(left == right)

    return finish

class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:

        for i in range(N):
            cells = advance_prison(cells)

        return cells

# better inplace soln, uses intermediate states
# 0 - empty, 1 - full
# intermediates
# "2 (was empty, will be empty)"
# "3 (was empty, will be full)"
# "4 (was full, will be empty)"
# "5 (was full, will be full)"
def advance_prison(cells):

    refstates=[
        [2,3],
        [4,5]
    ]

    for i in range(len(cells)):
        val = cells[i]
        if i == 0 or i == len(cells) - 1:
            if val == 0:
                cells[i] = 2
            else:
                cells[i] = 4
        else:
            left = cells[i-1]
            right = cells[i+1]
            was = val
            willbe = int((left > 3) == right)
            cells[i] = refstates[was][willbe]

        
    for i in range(len(cells)):
        val = cells[i]
        cells[i] = val % 2 # yay, our intermediate 'will be zero states' are even

    return

class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:

        state_ref = {}
        i=N
        while i > 0:
            state_ref[tuple(cells)] = i
            advance_prison(cells)
            i -= 1

            if state_ref.get(tuple(cells), None) is not None:
                t = state_ref[tuple(cells)]
                delta = t - i
                i %= delta

        return cells


# compromise the two (EDIT ADD CYCLE DETECTION)
def advance_prison(start, finish):

    for i in range(len(start)):
        if i == 0 or i == len(start)-1:
            finish[i] = 0
        else:
            left = start[i-1]
            right = start[i+1]
            finish[i] = int(left == right)

    return

class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        start = cells
        finish = cells[::]
        temp = None

        state_ref = {}

        i=N
        while i > 0:
            state_ref[tuple(start)] = i
            advance_prison(start, finish)
            temp = start
            start = finish
            finish = temp
            i -= 1

            if state_ref.get(tuple(start), None) is not None:
                t = state_ref[tuple(start)]
                delta = t - i
                i %= delta

        return start


# best overall
def advance_prison(cells):

    refstates=[
        [2,3],
        [4,5]
    ]

    for i in range(len(cells)):
        val = cells[i]
        if i == 0 or i == len(cells) - 1:
            if val == 0:
                cells[i] = 2
            else:
                cells[i] = 4
        else:
            left = cells[i-1]
            right = cells[i+1]
            was = val
            willbe = int((left > 3) == right)
            cells[i] = refstates[was][willbe]

        
    for i in range(len(cells)):
        val = cells[i]
        cells[i] = val % 2 # yay, our intermediate 'will be zero states' are even

    return

class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        N = N % 14
        if not N:
            N = 14
            
        for _ in range(N):
            advance_prison(cells)

        return cells