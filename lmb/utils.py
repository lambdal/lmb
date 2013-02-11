#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
    utils.py
    ~~~~~

    :created: 2013-02-10 23:16:24 -0800
    :copyright: (c) 2013. Lambda Labs, Inc.
    :license: BSD. See LICENSE.
"""
import urllib2
import cStringIO
from urlparse import urlparse
from PIL import Image as PILImage

def file_url(url):
    """
    url -> file
    """
    with closing(urllib2.urlopen(url)) as u:
        f = cStringIO.StringIO(u.read())
    return f

def file_fpath(fpath):
    return open(fpath)

def file_path(path):
    """
    path(url || filepath) -> file
    """
    parsed = urlparse(path)
    if 'http' in parsed.scheme:
        return file_url(path)
    else: # file
        return open(path)

def pil_path(path):
    """
    Make a PIL Image given a URL/fname
    """
    pi = PILImage.open(file_url(path))
    return pi

