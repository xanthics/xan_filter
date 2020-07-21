# xan_filter
**SoundPack** [Download](soundpack.zip?raw=true) 

Download, unzip archive, and place wav files in same directory as the filter

**HIDE** <a href="xan.t.hide.filter?raw=true" download>Download</a>

*Or*

**SHOW** <a href="xan.t.show.filter?raw=true" download>Download</a>

This is a script to generate a filter file for Path of Exile using the included config files.

Usage
=====
Run setup.py first to install all requirements.txt modules

Edit gen_always_highlight_currency.py (optional) in the first function with your account name, currency tab index, and POESESSID to have the filter tailor some highlighting to your account.

Run Create_filter with necessary config files to generate xan.filter.  Note that this will automatically put xan.show.filter and xan.hide.filter in <relative path>\Documents\My Games\Path of Exile

~~(Optional) Run pricetool to update currency, divination, essence, and unique tiers.  The poe ninja version should finish very quickly~~  

Config
======
See item_config.template.py and theme_config.minimal.py

Hide all
========
![Hide unspecified items](hide.png "Hide")

Show all
========
![Show all items](show.png "Show")

Thanks
======
This script is heavily inspired by "One Filter to rule them all" that can be found at https://www.pathofexile.com/forum/view-thread/1259059
