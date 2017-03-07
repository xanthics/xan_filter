#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher
desc = "Recipe Item"

# Base type : settings pair
items = {
    "0 rare hammers q>=16": {"base": "Stone Hammer\" \"Rock Breaker\" \"Gavel", "other": ["Rarity Rare", "Quality >= 16"], "type": "recipe item normal"},
    "0 magic hammers q>=12": {"base": "Stone Hammer\" \"Rock Breaker\" \"Gavel", "other": ["Rarity Magic", "Quality >= 12"], "type": "recipe item normal"},
    "0 normal hammers": {"base": "Stone Hammer\" \"Rock Breaker\" \"Gavel", "other": ["Rarity Normal"], "type": "recipe item normal"}
}