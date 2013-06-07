#!/usr/bin/env python

import plistlib


# rgb_to_hex by http://stackoverflow.com/a/214657
def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb


def plist_to_tuple(clr):
    rkey = 'Red Component'
    bkey = 'Blue Component'
    gkey = 'Green Component'
    return round(clr[rkey]*255), round(clr[gkey]*255), round(clr[bkey]*255)


def format_terminator(bg, fg, csr, pallete):
    conf = "{0}\n{1}\n{2}\n{3}".format('background_color="{0}"'.format(bg),
                                       'foreground_color="{0}"'.format(fg),
                                       'cursor_color="{0}"'.format(csr),
                                       'pallete="{0}"'.format(':'.join(pallete)))
    return conf


def main():
    plist = plistlib.readPlist('symfony.itermcolors')

    bg_rgb = plist_to_tuple(plist['Background Color'])
    bg_hex = rgb_to_hex(bg_rgb)
    fg_rgb = plist_to_tuple(plist['Foreground Color'])
    fg_hex = rgb_to_hex(fg_rgb)
    csr_rgb = plist_to_tuple(plist['Cursor Color'])
    csr_hex = rgb_to_hex(csr_rgb)

    pallete_hex = []
    for index in range(0, 16):
        color_key = "Ansi {0} Color".format(index)
        color_rgb = plist_to_tuple(plist[color_key])
        color_hex = rgb_to_hex(color_rgb)
        pallete_hex.append(color_hex)

    print format_terminator(bg_hex, fg_hex, csr_hex, pallete_hex)

if __name__ == "__main__":
    main()
