import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from pelicanconf import *

SITEURL = 'https://neogeny.github.io/blog'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True