#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Downloads the NASA Image of the Day (IOTD)
# http://www.nasa.gov/multimedia/imagegallery/iotd.html
# Outputs the title and description on CLI (handy for a cronjob)
#
# A lot of Code has been copied from
# • http://stackoverflow.com/a/22776
# • http://stackoverflow.com/a/3947241
# • http://stackoverflow.com/a/7406369
#
# Lars Weiler <lars@konvergenzfehler.de>
# CC0 2014-02-09


import os
import gzip
import urllib2
from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
from StringIO import StringIO

feed = 'http://www.nasa.gov/rss/lg_image_of_the_day.rss'
store_path = os.path.join('/','Users','Shared','NASA')

request = urllib2.Request(feed)
request.add_header('Accept-encoding', 'gzip')
response = urllib2.urlopen(request)

if response.info().get('Content-Encoding') == 'gzip':
    buf = StringIO(response.read())
    f = gzip.GzipFile(fileobj=buf)
    data = f.read()
else:
    data = response
    
s = BeautifulSoup(data)

for item in s.find_all('item'):
    image_url = item.enclosure['url']

    #file_name = image_url.split('/')[-1]
    file_name = (item.title.get_text() + '.' + image_url.split('.')[-1])
    keepcharacters = (' ','.','_')
    file_name =  "".join(c for c in file_name if c.isalnum() or c in keepcharacters).rstrip()
    fullfile = os.path.join(store_path, file_name)

    if not os.path.exists(fullfile):
        i = urllib2.urlopen(image_url)
        f = open(fullfile, 'wb')
        meta = i.info()
        file_size = int(meta.getheaders("Content-Length")[0])

        print "\n"
        print item.title.get_text()
        print "\n"
        print item.description.get_text()
        print "\n"
        print("Downloading: %s into %s, Bytes: %s" % (image_url, fullfile, file_size))
        
        file_size_dl = 0
        block_sz = 8192
        while True:
            buffer = i.read(block_sz)
            if not buffer:
                print('abort')
                break
    
            file_size_dl += len(buffer)

            f.write(buffer)
            status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
            status = status + chr(8)*(len(status)+1)
            print(status),
    
        f.close()

