"""
* Copyright (c) 2015 Jeremy Parks. All rights reserved.
*
* Permission is hereby granted, free of charge, to any person obtaining a
* copy of this software and associated documentation files (the "Software"),
* to deal in the Software without restriction, including without limitation
* the rights to use, copy, modify, merge, publish, distribute, sublicense,
* and/or sell copies of the Software, and to permit persons to whom the
* Software is furnished to do so, subject to the following conditions:
*
* The above copyright notice and this permission notice shall be included in
* all copies or substantial portions of the Software.
*
* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
* IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
* FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
* AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
* LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
* FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
* DEALINGS IN THE SOFTWARE.

Author: Jeremy Parks
Purpose: Create an item filter based on config files
Note: Requires Python 3.4.x
"""

import chance
import hide
import show
import currency
import gems
import uniques
import maps
import divination
import chroma
import flask
import rares
import rare_highlight


def gen_list(obj):
    b = ""

    # gen our string
    for i in sorted(obj.items):
        s = obj.items[i]
        if s['type'] != "ignore":
            b += "#{} - {}\n".format(i, obj.desc)
            if s['type'] == "hide":
                b += "Hide"
            else:
                b += "Show"
            if 'base' in s:
                b += "\n\tBaseType \"{}\"".format(s['base'])
            if 'class' in s:
                b += "\n\tClass \"{}\"".format(s['class'])
            if 'other' in s:
                b += "\n\t{}".format("\n\t".join(s['other']))
            if obj.settings[s['type']]:
                b += "\n\t{}".format("\n\t".join(obj.settings[s['type']]))
            b += "\n\n"

    return b


# main function for creating a filter
def main():
    buffer = ""

    buffer += gen_list(show)  # Always show these items
    buffer += gen_list(hide)  # Always hide these items
    buffer += gen_list(currency)  # Currency
    buffer += gen_list(gems)  # Gems
    buffer += gen_list(uniques)  # uniques
    buffer += gen_list(maps)  # maps
    buffer += gen_list(divination)  # divination cards
    buffer += gen_list(flask)  # Flasks
    buffer += gen_list(rare_highlight)  # rares
    buffer += gen_list(rares)  # rares
    buffer += gen_list(chroma)  # chrome vendor items
#    buffer += gen_list(chance)  # Chance bases
    buffer += "Show\n\tItemLevel <= 5\n\tSetFontSize 28\n\tSetBackgroundColor 0 0 0 100\n\tSetBorderColor 100 100 100"

    with open("xan.show.filter", "w") as f:
        f.write(buffer)
        # Default for all other items
        f.write("Show\n\tSetFontSize 18\n\tSetBackgroundColor 0 0 0 100\n\tSetBorderColor 100 100 100")

    with open("xan.hide.filter", "w") as f:
        f.write(buffer)
        # Default for all other items
        f.write("Hide\n\tSetFontSize 18\n\tSetBackgroundColor 0 0 0 100\n\tSetBorderColor 100 100 100")


if __name__ == "__main__":
    main()
