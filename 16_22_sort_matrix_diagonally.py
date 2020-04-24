# this isn't actually what the problem wants
# it is nice though
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:

        vals = sorted([v for row in mat for v in row], reverse=True)
        rows = len(mat)
        cols = len(mat[0])

        ls = min(rows, cols)
        for i in range(ls):
            dcon = True
            rcon = True
            mat[i][i] = vals.pop()

            roff = 1
            doff = 1
            while dcon and rcon:
                if i+doff < rows:
                    mat[i+doff][i] = vals.pop()
                    doff += 1
                else:
                    dcon = False
                
                if i + roff < cols:
                    mat[i][i+roff] = vals.pop()
                    roff += 1
                else:
                    rcon = False
        return mat

# here's an awesome one from junaid mansuri
class Solution:
    def diagonalSort(self, G: List[List[int]]) -> List[List[int]]:
        M, N, D = len(G), len(G[0]), collections.defaultdict(list)
        for i,j in itertools.product(range(M),range(N)): D[i-j].append(G[i][j])
        for k in D: D[k].sort(reverse = True)
        return [[D[i-j].pop() for j in range(N)] for i in range(M)]
