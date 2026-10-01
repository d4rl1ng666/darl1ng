# швейцария 

RESET = '\u001b[0m'
RED = '\u001b[41m'
WHITE = '\u001b[47m'

def flag():
    size = 11
    half_width_of_the_cross = 2
    center = size // 2
    for row in range(size):
        line = ''
        for col in range(size):
            vertical = (abs(col - center) <= half_width_of_the_cross // 2) and (2 <= row <= size - 3)
            horizontal = (abs(row - center) <= half_width_of_the_cross // 2) and (2 <= col <= size - 3)
            if horizontal or vertical:
                line += f"{WHITE}  "
            else: 
                line += f"{RED}  "
        print(f"{line}{RESET}")

flag()
