#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
# from mdx_grid_tables import GridTableExtension

AUTHOR = u'Carson J. Q. Farmer'
SITENAME = u'Carson Farmer'
SITEURL = u'http://carsonfarmer.com'
SITESUBTITLE = u'carsonfarmer.com'

GOOGLE_ANALYTICS = "UA-41110370-1"

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'
AUTHOR_EMAIL = "carsonfarmer@gmail.com"

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

TIMEZONE = 'US/Eastern'
TYPOGRIFY = True
DEFAULT_LANG = u'en'

LATEX = 'article'
IGNORE_FILES = ['.#*', '*~']

MARKUP = ("md", "ipynb")

PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = ['gravatar', 'latex', 'summary', 'liquid_tags.notebook',
           'liquid_tags.youtube', 'liquid_tags.vimeo', 'liquid_tags.img',
           'liquid_tags.gram', 'liquid_tags.include_code', 'tipue_search']

NOTEBOOK_DIR = 'notebooks'

SUMMARY_END_MARKER = "<!--more-->"

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/%s.atom.xml"
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

# Theme and style information
THEME = "themes/carson"
#CSS_FILE = "wide.css"

MD_EXTENSIONS = (['codehilite(css_class=highlight)', 'extra', 'fenced_code', ])

# Some useful defaults and menu settings
DEFAULT_CATEGORY = 'News'
DEFAULT_DATE_FORMAT = '%a %d %B %Y'
DISPLAY_PAGES_ON_MENU = True
DISPLAY_HOME_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

DISQUS_SITENAME = "carsonfarmer"

# Which folders should be copied to output
STATIC_PATHS = ['images', 'uploads', 'libs/bootstrap-3.1.1/dist',
                'extras/favicon.ico', 'extras/CNAME', 'examples',
                'libs/leaflet', 'extras/visitors_map.js', 'libs/cartogram',
                'extras/map-thumb.png', 'libs/tipuesearch']

EXTRA_PATH_METADATA = {
    'extras/favicon.ico': {'path': 'favicon.ico'},
    'extras/CNAME': {'path': 'CNAME'},
    'extras/visitors_map.js': {'path': 'uploads/visitors_map.js'},
    'extras/map-thumb.png': {'path': 'uploads/map-thumb.png'},
    'examples': {'path': 'examples'},
}

PAGE_EXCLUDES = ["libs"]
ARTICLE_PATHS = ["blog"]
ARTICLE_EXCLUDES = ["pages", "libs"]

SUMMARY_MAX_LENGTH = 100

# Social widget
SOCIAL = (
    ('twitter', 'https://twitter.com/carsonfarmer', 'fa-twitter'),
    ('github', 'https://github.com/carsonfarmer', 'fa-github'),
    ('about.me', 'http://about.me/carsonfarmer', 'fa-user'),
    # ('academia.edu', 'http://hunter-cuny.academia.edu/CarsonFarmer','fa -book'),
    ('linkedin', 'http://www.linkedin.com/pub/carson-farmer/40/3bb/27/','fa-linkedin'),
    ('google+', 'https://plus.google.com/108062014159451325697/about/p/pub','fa-google-plus'),
    # ('cuny.is', 'http://cuny.is/cfarmer', 'fa-comment-o'),
    ('email', 'mailto:carsonfarmer@gmail.com', 'fa-envelope'),
)

TWITTER_USERNAME = 'carsonfarmer'
TWITTER_WIDGET_ID = '460846751906144256'
DEFAULT_PAGINATION = 8

RELATIVE_URLS = True
