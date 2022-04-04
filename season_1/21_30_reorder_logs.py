def create_identifier(log):
    toks = log.split()
    
    prefix = int(toks[1].isnumeric())
    addin = ''
    if prefix == 0:
        addin = f"{' '.join(toks[1:])} {toks[0]}"
    return f"{prefix} {addin}"

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        logs.sort(key=create_identifier)
        return logs