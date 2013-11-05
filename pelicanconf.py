#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Carson J. Q. Farmer'
SITENAME = u'Carson Farmer'
SITEURL = u'http://www.carsonfarmer.com'
SITESUBTITLE = u'www.carsonfarmer.com'

GOOGLE_ANALYTICS = "UA-41110370-1"

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'
AUTHOR_EMAIL = "carson.farmer@gmail.com"

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

TIMEZONE = 'US/Eastern'
TYPOGRIFY = True
DEFAULT_LANG = u'en'

LATEX = 'article'
IGNORE_FILES = ['.#*', '*~']

MARKUP = ("md", "ipynb")

PLUGIN_PATH = "pelican-plugins/"
PLUGINS = ['gravatar', 'latex', 'summary', 'liquid_tags.notebook']

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

MD_EXTENSIONS = (['codehilite(css_class=highlight)','extra', 'fenced_code'])

# Some useful defaults and menu settings
DEFAULT_CATEGORY = 'News'
DEFAULT_DATE_FORMAT = '%a %d %B %Y'
DISPLAY_PAGES_ON_MENU = False
DISPLAY_HOME_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

MENUITEMS = (('About', 'about/', 'icon-info-sign'), 
             ('Curriculum Vitae', 'curriculum-vitae/', 'icon-rocket'),
             ('Work','links', 'icon-globe'),)

DISQUS_SITENAME = "carsonfarmer"

# Which folders should be copied to output/static
STATIC_PATHS = ['images', 'uploads', 'libs', 'javascipt', 
                'extras/favicon.ico', 'extras/404.html',
                'extras/CNAME', 'examples'
               ]

EXTRA_PATH_METADATA = {'extras/favicon.ico': {'path': 'favicon.ico'},
                       'extras/404.html': {'path': '404.html'},
                       'extras/CNAME': {'path': 'CNAME'},
                       'examples' : {'path': 'examples'}
                      }

# Blogroll
LINKS =  (('Research','research/','icon-bar-chart'),
          ('Software', 'spatial-software/','icon-code'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/CarsonFarmer', 'icon-twitter'),
          ('github', 'https://github.com/cfarmer', 'icon-github'),
          ('about.me', 'http://about.me/carson.farmer', 'icon-user'),
          ('academia.edu', 'http://hunter-cuny.academia.edu/CarsonFarmer','icon-book'),
          ('linkedin', 'http://www.linkedin.com/pub/carson-farmer/40/3bb/27/','icon-linkedin'),
          ('google+', 'https://plus.google.com/108062014159451325697/about/p/pub','icon-google-plus'),
          ('cuny.is', 'http://cuny.is/cfarmer', 'icon-comment-alt'),
          ('email', 'mailto:carson.farmer@gmail.com', 'icon-envelope'),)

TWITTER_USERNAME = 'CarsonFarmer'
TWITTER_WIDGET_ID = '330339195518337025'
DEFAULT_PAGINATION = 8

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
