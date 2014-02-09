NASA-IOTD
=========

NASA Image of the Day Downloader

http://www.nasa.gov/multimedia/imagegallery/iotd.html

Downloads the NASA Image of the Day from the RSS-Feed. NASA switched to a new style of RSS Feed in December 2013, with RSS instead of HTML elements. My oldstyle Mac OS X Automator Script could not parse the Image URLs. Furthermore some of their servers deliver gzipped data instead of uncompressed text, which made some other scripts run crazy.

This script will download the image and rename the file to the title (with safe characters). An existing file will be skipped. The RSS contains the recent 10 days of images, so the script does not need to be run daily. The script will also output the title and the description. This is quite handy for cron jobs where you receive an email.

Requirements
------------

* `easy_install beautifulsoup4`
* change `store_path` in the script

Acknowledgement
---------------

Most of the code has been copied from
* http://stackoverflow.com/a/22776
* http://stackoverflow.com/a/3947241
* http://stackoverflow.com/a/7406369

License
-------
CC0 http://creativecommons.org/publicdomain/zero/1.0/
