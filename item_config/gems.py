#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher
desc = "gems"

# Base type : settings pair
items = {
    "01 Quality Gem 20": {"class": "Gems", "other": ["Quality 20"], "type": "currency high"},
    "02 Quality Gem High": {"class": "Gems", "other": ["Quality >= 10"], "type": "gem very high"},
    "03 Quality Gem": {"class": "Gems", "other": ["Quality >= 1"], "type": "gem high"},
    "1 Portal": {"base": "Portal", "class": "Gems", "type": "gem normal"},
    "1 Detonate Mines": {"base": "Detonate Mines", "class": "Gems", "type": "gem low"},
    "1 Empower": {"base": "Empower", "class": "Gems", "type": "gem normal"},
    "1 Enhance": {"base": "Enhance", "class": "Gems", "type": "ignore"},
    "1 Enlighten": {"base": "Enlighten", "class": "Gems", "type": "gem normal"},
    "1 Added Chaos Damage": {"base": "Added Chaos Damage", "class": "Gems", "type": "gem normal"},
    "1 Vaal Gems": {"base": "Vaal", "class": "Gems", "type": "gem low"},
    "9 Other Gems": {"class": "Gems", "type": "ignore"}
}