import curses
import time

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "Press 'q' to exit.")
        stdscr.refresh()

        key = stdscr.getch()
        if key == ord('q'):
            break

if __name__ == "__main__":
    curses.wrapper(main)