#!/usr/bin/env python

import plistlib
import sys
from os import listdir
from os.path import isfile, isdir, splitext, join


# rgb_to_hex by http://stackoverflow.com/a/214657
def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb


# TODO: wrong conversion. iTerm uses sRGB
def iterm_to_rgb(clr):
    rkey = 'Red Component'
    bkey = 'Blue Component'
    gkey = 'Green Component'
    return round(clr[rkey]*255), round(clr[gkey]*255), round(clr[bkey]*255)


def format_terminator(bg, fg, csr, pallete, indent):
    #TODO: do something for the indent. its ugly
    conf = "{4}{0}\n{4}{1}\n{4}{2}\n{4}{3}".format('background_color = "{0}"'.format(bg),
                                                   'foreground_color = "{0}"'.format(fg),
                                                   'cursor_color = "{0}"'.format(csr),
                                                   'palete = "{0}"'.format(':'.join(pallete)),
                                                   ' '*indent)
    return conf


def to_terminator(itermcolors, indent=0):
    plist = plistlib.readPlist(itermcolors)

    bg_hex = rgb_to_hex(iterm_to_rgb(plist['Background Color']))
    fg_hex = rgb_to_hex(iterm_to_rgb(plist['Foreground Color']))
    csr_hex = rgb_to_hex(iterm_to_rgb(plist['Cursor Color']))

    pallete_hex = []
    for index in range(0, 16):
        color_key = "Ansi {0} Color".format(index)
        color_rgb = iterm_to_rgb(plist[color_key])
        color_hex = rgb_to_hex(color_rgb)
        pallete_hex.append(color_hex)

    return format_terminator(bg_hex, fg_hex, csr_hex, pallete_hex, indent)


def raise_error(msg):
    instruction = """Usage: ./convert.py <file|directory>
Accepts .itermcolors file or a directory containing .itermcolors files as argument.
The conversion results will be written to stdout.

Example: ./convert.py symfony.itermcolors
         ./convert.py ~/iTerm-2-Color-Themes > terminatorschemes.txt"""
    print msg + "\n"
    print instruction
    sys.exit(1)


def main(args):
    if isdir(args[1]):
        path = args[1]
        confs = ""
        for f in listdir(path):
            abs_path = join(path, f)
            splitname = splitext(f)
            if isfile(abs_path) and splitname[1] == ".itermcolors":
                confs += "[[{0}]]\n".format(splitname[0])
                confs += to_terminator(abs_path, 2) + "\n\n"
        if confs == "":
            raise_error("No itermcolors found in the directory.")
        else:
            print confs
    elif isfile(args[1]):
        if(splitext(args[1])[1] == ".itermcolors"):
            print to_terminator(args[1])
        else:
            raise_error("Invalid itermcolors file")
    else:
        raise_error("Error parsing argument")


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        raise_error("Invalid argument")
    else:
        main(args)
