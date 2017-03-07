#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher
desc = "General Rares"

# Base type : settings pair
items = {
    "1 Quiver": {"class": "Quivers", "type": "rare low"},

    "7 5": {"other": ["DropLevel <= 5", "ItemLevel >= 15"], "type": "rare low"},
    "7 10": {"other": ["DropLevel <= 10", "ItemLevel >= 20"], "type": "rare low"},
    "7 15": {"other": ["DropLevel <= 15", "ItemLevel >= 25"], "type": "rare low"},
    "7 20": {"other": ["DropLevel <= 20", "ItemLevel >= 30"], "type": "rare low"},
    "7 25": {"other": ["DropLevel <= 25", "ItemLevel >= 35"], "type": "rare low"},
    "7 30": {"other": ["DropLevel <= 30", "ItemLevel >= 40"], "type": "rare low"},
    "7 35": {"other": ["DropLevel <= 35", "ItemLevel >= 45"], "type": "rare low"},
    "7 40": {"other": ["DropLevel <= 40", "ItemLevel >= 50"], "type": "rare low"},
    "7 45": {"other": ["DropLevel <= 45", "ItemLevel >= 55"], "type": "rare low"},

    "9 Other rares": {"type": "rare low"}
}