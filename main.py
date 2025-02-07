import curses

def main(stdscr):
    curses.curs_set(0)
    stdscr.addstr(0, 0, "Press any key to exit.")
    stdscr.refresh()
    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)