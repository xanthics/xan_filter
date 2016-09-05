# poe_filter

This is a script to generate a filter file for Path of Exile using the included config files.

[GGG Forum thread](https://www.pathofexile.com/forum/view-thread/1721195) with more information about the filter.

**HIDE**
* [Download Essence](xan.e.hide.filter?raw=true)
* [Download Essence Hardcore](xan.ehc.hide.filter?raw=true)
* [Download Standard](xan.st.hide.filter?raw=true)
* [Download Hardcore](xan.hc.hide.filter?raw=true)

**SHOW**
* [Download Essence](xan.e.show.filter?raw=true)
* [Download Essence Hardcore](xan.ehc.show.filter?raw=true)
* [Download Standard](xan.s.show.filter?raw=true)
* [Download Hardcore](xan.hc.show.filter?raw=true)

Usage
=====
Run Create_filter with necessary config files to generate xan.filter.  Note that this will automatically put xan.show.filter and xan.hide.filter in <relative path>\Documents\My Games\Path of Exile

(Optional) Run pricetool to update divination and unique tiers.  This may take some time depending on how much data is pending in ggg stash river.  Requires a running MongoDB instance.

Config
======
See item_config.template.py and theme_config.minimal.py

Hide all
========
![Hide unspecified items](https://i.imgur.com/4787erv.jpg "Hide")

Show all
========
![Show all items](https://i.imgur.com/AeFb9UM.jpg "Show")

Thanks
======
This script is heavily inspired by "One Filter to rule them all" that can be found at https://www.pathofexile.com/forum/view-thread/1259059
