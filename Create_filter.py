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
import special
import maps
import divination
import chroma
import flask
import rares

def gen_list(obj):
    b = ""

    # gen our string
    for i in sorted(obj.items):
        s = obj.items[i]
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
    with open("xan.filter", "w") as f:
        #Show ignoring other catagories
        f.write(gen_list(special))

        # Always hide these items
        f.write(gen_list(hide))

        # Currency
        f.write(gen_list(currency))

        # Gems
        f.write(gen_list(gems))

        # uniques
        f.write(gen_list(uniques))

        # maps
        f.write(gen_list(maps))

        # divination cards
        f.write(gen_list(divination))

        # Flasks
        f.write(gen_list(flask))

        # Chance bases
        f.write(gen_list(chance))

        # rares
        f.write(gen_list(rares))

        # Always show these items
        f.write(gen_list(show))

        # chrome vendor items
        f.write(gen_list(chroma))

        # Default for all other items
        f.write("Hide\n\tSetFontSize 18\n\tSetBackgroundColor 0 0 0 100\n\tSetBorderColor 100 100 100")
        # f.write("Show\n\tSetFontSize 18\n\tSetBackgroundColor 0 0 0 100\n\tSetBorderColor 100 100 100")


if __name__ == "__main__":
    main()
