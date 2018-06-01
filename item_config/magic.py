#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher
desc = "Magic items"

# Base type : settings pair
items = {
	"0 magic item": {"other": ["Class Dagger Wand \"One Hand\" Bow Stave \"Two Hand\" Sceptre Claws", "Rarity Magic", "SetBorderColor 208 32 144", "Identified True"], "type": "hide"},
}

# TODO: expand this section for better creation of mods/bases to look at
def magicmods():

	ret = {"Magic Items": {"other": ['HasExplicitMod "Tacati\'s" "Citaqualotl\'s" "Matatl\'s" "Topotante\'s" "Xopec\'s" "Guatelitzi\'s" "of Tacati" "of Citaqualotl" "of Matatl" "of Puhuarte" "of Guatelitzi" "Brinerot" "Mutewind" "Redblade" "Betrayer\'s" "Deceiver\'s" "Turncoat\'s" "Tyrannical" "Merciless" '
					 '"Electrocuting" "Resplendent" "Incandescent" "Rapturous" "Prime" "Vigorous" "Virile" "Overpowering" "of the Rainbow" "of Ephij" "of Haast" "of Tzteosh"'], "type": "show normal"}}

	return ret