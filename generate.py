#!/usr/bin/env python3

import argparse
from PIL import Image
import random

def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def main(path, d):
    src_file = Image.open(path)
    pixels = src_file.load()
    x, y = src_file.size
    res_str = ''
    j = 1
    while j <= y-1:
        i = 1
        while i <= x-1:
            res_str += '<p style="color: {}; margin: 0px; padding: 0px; display: inline;">{}</p>'.format(rgb2hex(*pixels[i, j]), random.randint(0, 1))
            i += d
        res_str += '<br>\n'
        j += d*2
    with open('result.html', 'w') as res_file:
        res_str = '<html><head><title>Result symbol image</title></head><body style="background: #000000;">{}</body></html>'.format(res_str)
        res_file.write(res_str)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Symbol images generator')
    parser.add_argument('path', help='path to source file')
    parser.add_argument('-d', default=3, help='seek pixels')
    args = parser.parse_args()
    main(args.path, int(args.d))
    print('Success!')
