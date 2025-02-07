import curses
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
    pattern = [[' ' for _ in range(cols)] for _ in range(rows)]
    pattern[rows // 2][cols // 2] = '*'
    return pattern

if __name__ == "__main__":
    curses.wrapper(main)