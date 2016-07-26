#!/usr/bin/python
# -*- coding: utf-8 -*-
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

desc = "Animate Weapon target"

# types intended for this is "animate melee" and "animate range"

# Base type : settings pair
items = {
	"0 animate melee white 4x1": {"other": ["Class Dagger \"One Hand\" Stave \"Two Hand\" Sceptre Claws", "Rarity Normal", "Height 4", "Width 1"], "type": "ignore"},
	"0 animate range white 4x1": {"other": ["Class Wand Bow", "Rarity Normal", "Height 4", "Width 1"], "type": "ignore"},
	"0 animate melee magic 4x1": {"other": ["Class Dagger \"One Hand\" Stave \"Two Hand\" Sceptre Claws", "Rarity Magic", "Height 4", "Width 1", "Identified True"], "type": "ignore"},
	"0 animate range magic 4x1": {"other": ["Class Wand Bow", "Rarity Magic", "Height 4", "Width 1", "Identified True"], "type": "ignore"},

	"0 animate melee white 3x1": {"other": ["Class Dagger \"One Hand\" Stave \"Two Hand\" Sceptre Claws", "Rarity Normal", "Height 3", "Width 1"], "type": "ignore"},
	"0 animate range white 3x1": {"other": ["Class Wand Bow", "Rarity Normal", "Height 3", "Width 1"], "type": "ignore"},
	"0 animate melee magic 3x1": {"other": ["Class Dagger \"One Hand\" Stave \"Two Hand\" Sceptre Claws", "Rarity Magic", "Height 3", "Width 1", "Identified True"], "type": "ignore"},
	"0 animate range magic 3x1": {"other": ["Class Wand Bow", "Rarity Magic", "Height 3", "Width 1", "Identified True"], "type": "ignore"},

	"0 animate melee white 2x2": {"other": ["Class Dagger \"One Hand\" Stave \"Two Hand\" Sceptre Claws", "Rarity Normal", "Height 2", "Width 2"], "type": "ignore"},
	"0 animate range white 2x2": {"other": ["Class Wand Bow", "Rarity Normal", "Height 2", "Width 2"], "type": "ignore"},
	"0 animate melee magic 2x2": {"other": ["Class Dagger \"One Hand\" Stave \"Two Hand\" Sceptre Claws", "Rarity Magic", "Height 2", "Width 2", "Identified True"], "type": "ignore"},
	"0 animate range magic 2x2": {"other": ["Class Wand Bow", "Rarity Magic", "Height 2", "Width 2", "Identified True"], "type": "ignore"},

	"1 animate melee white": {"other": ["Class Dagger \"One Hand\" Stave \"Two Hand\" Sceptre Claws", "Rarity Normal"], "type": "ignore"},
	"1 animate range white": {"other": ["Class Wand Bow", "Rarity Normal"], "type": "ignore"},
	"1 animate melee magic": {"other": ["Class Dagger \"One Hand\" Stave \"Two Hand\" Sceptre Claws", "Rarity Magic", "Identified True"], "type": "ignore"},
	"1 animate range magic": {"other": ["Class Wand Bow", "Rarity Magic", "Identified True"], "type": "ignore"},
}