import curses
import random
import time

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()
        stdscr.addstr(0, 0, f"Size: {width}x{height}. Press 'q' to exit.")
        stdscr.refresh()

        key = stdscr.getch()
        if key == ord('q'):
            break

def generate_pattern(rows, cols):
    symbols = ['*', '+', '.', 'o', 'x']
    pattern = [[' ' for _ in range(cols)] for _ in range(rows)]

    for _ in range((rows * cols) // 20):
        y = random.randint(0, rows // 2 - 1)
        x = random.randint(0, cols // 2 - 1)
        symbol = random.choice(symbols)

        pattern[y][x] = symbol
        pattern[y][cols - x - 1] = symbol
        pattern[rows - y - 1][x] = symbol
        pattern[rows - y - 1][cols - x - 1] = symbol

    return pattern

def render_pattern(stdscr, pattern):
    for y, row in enumerate(pattern):
        for x, char in enumerate(row):
            stdscr.addch(y, x, char)

if __name__ == "__main__":
    curses.wrapper(main)