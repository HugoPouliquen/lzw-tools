# -*- coding: utf-8 -*-
import curses
from curses.textpad import Textbox, rectangle
from libs.curses_browser import open_tty
from libs.curses_browser import restore_stdio
from libs.curses_browser import main
from utils.compression import compress
from utils.compression import fileCompression
from utils.decompression import decompress
from utils.decompression import fileDecompression

"""
This is the cli with menu. For understand better read
Curses doc : https://docs.python.org/3/howto/curses.html
"""

def init_curses():
    stdsrc = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdsrc.keypad(1)
    return stdsrc


def close_curses(stdsrc):
    stdsrc.keypad(0)
    curses.nocbreak()
    curses.echo()
    curses.endwin()


def init_colors():
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_RED)


def display_menu(title, menu, window, active=1):
    window.addstr(1, 1, title, curses.color_pair(1))
    window.addstr(3, 1, "Choisissez ↓ ↑ : ")
    item_pos = 4
    pos = 1
    for item in menu:
        if pos == active:
            color = curses.color_pair(2)
        else:
            color = curses.A_NORMAL
        window.addstr(item_pos, 1, "   %d. %s" % (pos, item), color)
        item_pos += 1
        pos += 1

    window.refresh()


def getKey(final, title, menu, window, active_pos=1):
    c = None

    while c != 10:
        c = window.getch()
        if c == 66:
            if active_pos != final:
                active_pos += 1
            else:
                active_pos = 1
        elif c == 65:
            if active_pos != 1:
                active_pos -= 1
            else:
                active_pos = final
        display_menu(title, menu, window, active_pos)

    return active_pos

try:
    stdsrc = init_curses()
    init_colors()

    window = curses.newwin(19, 79, 3, 5)
    window.border(0)

    menu_list = ('Compression', 'Décompression', 'Quitter')
    title = 'LZW tools - Quelle sera votre voie ?'
    display_menu(title, menu_list, window)

    choice = getKey(len(menu_list), title, menu_list, window)

    if choice == 1:
            saved_fds, saved_stdout = open_tty()
            try:
                path = curses.wrapper(main) # launch new window
            finally:
                lzw = fileCompression(path)
                restore_stdio(saved_fds, saved_stdout)
                close_curses(stdsrc)
                print('Your content has compressed in:', lzw)
    elif choice == 2:
        saved_fds, saved_stdout = open_tty()
        try:
            path = curses.wrapper(main)
        finally:
            original = fileDecompression(path)
            restore_stdio(saved_fds, saved_stdout)
            close_curses(stdsrc)
            print('Your content has decompressed in:', original)
    window.addstr(
        17, 2, "Ce n'est qu'un au-revoir ! (Appuyez sur une touche tu dois)"
    )
    window.refresh()
    c = window.getch()
finally:
    close_curses(stdsrc)
