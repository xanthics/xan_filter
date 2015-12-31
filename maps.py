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

desc = "maps"

# Text settings for various categories
settings = {
    "very high": ["Class \"Maps\"",
                  "SetBorderColor 150 0 0",
                  "SetFontSize 42",
                  "PlayAlertSound 6 125"],
    "high": ["Class \"Maps\"",
             "PlayAlertSound 2 100",
             "SetFontSize 37"],
    "normal": ["Class \"Maps\""],
    "low": ["Class \"Maps\""],
    "ignore": [""],
    "hide": ["Class \"Maps\""]
}

# Base type : settings pair
items = {
    "01 Maps >= 79": {"other": ["DropLevel >= 79"], "type": "very high"},
    "02 Maps <= 73": {"other": ["DropLevel <= 73"], "type": "normal"},
    "03 Other maps": {"type": "high"},
    "04 Map Fragments": {"type": "normal"},
}