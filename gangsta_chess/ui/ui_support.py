#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 5.2
#  in conjunction with Tcl version 8.6
#    May 07, 2020 08:54:40 PM MDT  platform: Linux

py3 = True
w = None
top_level = None
root = None


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


if __name__ == '__main__':
    import ui
    ui.vp_start_gui()
