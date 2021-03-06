from curses import color_pair

cores = {
    'black': 1, 'blue': 5, 'cyan': 7, 'green': 3, 'red': 2,
    'white': 0, 'yellow': 4, 'purple': 6, 'gray': 9
}


def cor(cor: str):
    return color_pair(cores[cor])
