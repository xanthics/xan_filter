# poe_filter

This is a script to generate a filter file for Path of Exile using the included config files.

**HIDE**
* [Hide Download Essence](xan.essence.hide.filter?raw=true)
* [Hide Download Essence Hardcore](xan.essencehc.hide.filter?raw=true)
* [Hide Download Standard](xan.standard.hide.filter?raw=true)
* [Hide Download Hardcore](xan.hardcore.hide.filter?raw=true)

**SHOW**
* [Show Download Essence](xan.essence.show.filter?raw=true)
* [Show Download Essence Hardcore](xan.essencehc.show.filter?raw=true)
* [Show Download Standard](xan.standard.show.filter?raw=true)
* [Show Download Hardcore](xan.hardcore.show.filter?raw=true)

Usage
=====
Run Create_filter with necessary config files to generate xan.filter.  Note that this will automatically put xan.show.filter and xan.hide.filter in <relative path>\Documents\My Games\Path of Exile

~~(Optional) Run Exiletool to update divination and unique tiers.  You will need to create "api_key.py" first with user and password.  See [Exile Tool API](http://api.exiletools.com/info/) for an API key(password).~~

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
