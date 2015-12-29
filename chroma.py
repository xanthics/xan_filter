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

desc = "template"

# Text settings for various categories
settings = {
    "very high": ["SocketGroup RGB"],
    "high": ["SocketGroup RGB"],
    "normal": ["SocketGroup RGB",
               "SetBorderColor 27 162 155",
               "SetFontSize 28"],
    "low": ["SocketGroup RGB",
            "SetBorderColor 27 162 155",
            "SetFontSize 20"],
    "hide": ["SocketGroup RGB"]
}

# Base type : settings pair
items = {
    "01 4x1": {"other": ["Height 4", "Width 1"], "type": "normal"},
    "02 3x1": {"other": ["Height 3", "Width 1"], "type": "normal"},
    "03 2x2": {"other": ["Height 2", "Width 2"], "type": "normal"},
    "04 Other Chromes": {"type": "low"}
}
