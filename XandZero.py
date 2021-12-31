def is_tie(the_arena):
    return " " not in the_arena[0] and " " not in the_arena[1] and " " not in the_arena[2]


def is_game_finished(the_arena):
    def compare(a, b, c):
        if a == b == c and ' ' not in (a, b, c):
            return True

    is_finised = False

    is_finised = is_finised or compare(the_arena[0][0], the_arena[0][1], the_arena[0][2])
    is_finised = is_finised or compare(the_arena[1][0], the_arena[1][1], the_arena[1][2])
    is_finised = is_finised or compare(the_arena[2][0], the_arena[2][1], the_arena[2][2])
    is_finised = is_finised or compare(the_arena[0][0], the_arena[1][0], the_arena[2][0])
    is_finised = is_finised or compare(the_arena[0][1], the_arena[1][1], the_arena[2][1])
    is_finised = is_finised or compare(the_arena[0][2], the_arena[1][2], the_arena[2][2])
    is_finised = is_finised or compare(the_arena[0][0], the_arena[1][1], the_arena[2][2])
    is_finised = is_finised or compare(the_arena[0][2], the_arena[1][1], the_arena[2][0])

    return is_finised

def print_cell(cell_value):
    if cell_value == "0":
        color = CYAN
    elif cell_value == "x" or cell_value == "X":
        color = RED
    else:
        color = YELLOW
    print(color + cell_value + ENDC, end="")

def print_arena(arena):
    for arena_row in arena:  # iterate list seperate
        for element in arena_row:  # iterate the elements from the lists
            print("| ", end="")
            print_cell(element)
            print(" ", end="")
        print("|")

def get_arena_index_by_key(key):
    if key == "q":
        return 0, 0
    elif key == "w":
        return 0, 1
    elif key == "e":
        return 0, 2
    elif key == "a":
        return 1, 0
    elif key == "s":
        return 1, 1
    elif key == "d":
        return 1, 2
    elif key == "z":
        return 2, 0
    elif key == "x":
        return 2, 1
    elif key == "c":
        return 2, 2

def get_cell(the_arena, key):
    i, j = get_arena_index_by_key(key)
    return the_arena[i][j]

def set_cell(the_arena, key, char):
    i, j = get_arena_index_by_key(key)
    the_arena[i][j] = char

def new_game():
    the_arena = [[" ", " ", " ",], [" ", " ", " ",], [" ", " ", " ",]]
    print_arena(the_arena)
    char = 'x'

    while True:

        next_move = input("Enter next move: ")
        if next_move not in ["q", "w", "e", "a", "s", "d", "z", "x", "c"]:
            print("Wrong instructions please read the option settings")
            continue

        if get_cell(the_arena, next_move) != " ":
            print("You are a cheater, go fuck yourself")
            continue

        set_cell(the_arena, next_move, char)
        print_arena(the_arena)
        if is_game_finished(the_arena):
            print(f"{char} WON-YOU ARE FUCKING LEGEND")
            break

        if is_tie(the_arena):
            print("Is TIE, GO fuck yourselfs")
            break

        if char == "x":
            char = "0"
        elif char == "0":
            char = "x"



YELLOW = '\033[93m'
ENDC = '\033[0m'        # the end of the colors text
CYAN = '\033[96m'
RED = '\033[91m'

new_game()

