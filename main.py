import curses
import random
import time

def main(stdscr):
    curses.start_color()
    for i in range(1, 8):
        curses.init_pair(i, i, curses.COLOR_BLACK)

    draw_kaleidoscope(stdscr)

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

def draw_kaleidoscope(stdscr):
    frame = 0
    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()
        pattern = generate_pattern(height - 2, width - 2)

        for y in range(height - 2):
            for x in range(width - 2):
                stdscr.addch(y + 1, x + 1, pattern[y][x])

        stdscr.refresh()
        frame += 1
        time.sleep(0.1)

        if stdscr.getch() == ord('q'):
            break

if __name__ == "__main__":
    curses.wrapper(main)