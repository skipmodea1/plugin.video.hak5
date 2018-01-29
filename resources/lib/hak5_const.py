#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import os
import xbmc
import xbmcaddon
from bs4 import BeautifulSoup

#
# Constants
#
ADDON = "plugin.video.hak5"
SETTINGS = xbmcaddon.Addon()
LANGUAGE = SETTINGS.getLocalizedString
IMAGES_PATH = os.path.join(xbmcaddon.Addon().getAddonInfo('path'), 'resources', 'images')
HAK5RECENTLYADDEDURL = 'http://www.hak5.org/category/episodes'
HAK5SEASONSURLHTTPS = 'https://www.hak5.org/shows/hak5'
HAKTIKRECENTLYADDEDURL = 'http://www.hak5.org/category/episodes/haktip/page/001'
THREATWIRERECENTLYADDEDURL = 'http://www.hak5.org/category/episodes/threatwire/page/001'
TEKTHINGRECENTLYADDEDURL = 'http://www.hak5.org/category/episodes/tekthing/page/001'
PINEAPPLEUNIVERSITYRECENTLYADDEDURL = 'http://www.hak5.org/category/episodes/pineapple-university'
METASPLOITRECENTLYADDEDURL = 'http://www.hak5.org/category/episodes/metasploit-minute/page/001'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
DATE = "2018-01-29"
VERSION = "1.0.4-SNAPSHOT"

if sys.version_info[0] > 2:
    unicode = str


def convertToUnicodeString(s, encoding='utf-8'):
    """Safe decode byte strings to Unicode"""
    if isinstance(s, bytes):  # This works in Python 2.7 and 3+
        s = s.decode(encoding)
    return s


def convertToByteString(s, encoding='utf-8'):
    """Safe encode Unicode strings to bytes"""
    if isinstance(s, unicode):
        s = s.encode(encoding)
    return s


def log(name_object, object):
    try:
        xbmc.log("[ADDON] %s v%s (%s) debug mode, %s = %s" % (
            ADDON, VERSION, DATE, name_object, convertToUnicodeString(object)), xbmc.LOGDEBUG)
    except:
        xbmc.log("[ADDON] %s v%s (%s) debug mode, %s = %s" % (
            ADDON, VERSION, DATE, name_object,
            "Unable to log the object due to an error while converting it to an unicode string"), xbmc.LOGDEBUG)


def getSoup(html, default_parser="html5lib"):
    soup = BeautifulSoup(html, default_parser)
    return soup