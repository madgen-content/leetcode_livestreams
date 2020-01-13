def time_add(time_tup, hours, minutes):
    mins = time_tup[1]
    hrs = time_tup[0]

    initial = mins + minutes
    f_mins =  initial % 60
    carry = initial // 60
    f_hrs = hrs + hours + carry

    return (f_hrs, f_mins)

def explore_hour(allowed_digits, lit_digits, current_digit_location, digit_tups: list, base_tup: tuple):
    if allowed_digits == lit_digits:
        digit_tups.append(base_tup)
        return
    
    for i in range(2):
        new_base = time_add(base_tup, (2**current_digit_location) * i, 0)
        
        if new_base[0] > 11:
            continue

        if current_digit_location == 0:
            explore_minute(allowed_digits, lit_digits + i, 5, digit_tups, new_base)
        else:
            explore_hour(allowed_digits, lit_digits + i, current_digit_location - 1, digit_tups, new_base)
    return

def explore_minute(allowed_digits, lit_digits, current_digit_location, digit_tups: list, base_tup: tuple):
    if allowed_digits == lit_digits:
        digit_tups.append(base_tup)
        return
    
    for i in range(2):
        new_base = time_add(base_tup, 0, (2**current_digit_location) * i )

        if new_base[0] > 11:
            continue
        
        if current_digit_location == 0:
            digit_tups.append(new_base)
        else:
            explore_minute(allowed_digits, lit_digits + i, current_digit_location - 1, digit_tups, new_base)
    return

def process_tup(tup) -> str:
    fill = ""
    if tup[1] < 10:
        fill = "0"
    return f'{tup[0]}:{fill}{tup[1]}'

class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        time_tups = []
        explore_hour(num, 0, 3, time_tups, (0,0))
        ans = list(sorted([process_tup(x) for x in time_tups]))
        if len(ans) > 1:
            return ans[1:]
        else:
            return ans
        return