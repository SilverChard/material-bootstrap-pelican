#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from os import getenv

AUTHOR = 'Silver'
SITENAME = "Silver's Blog"

SITEURL = 'http://123.206.29.21/'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zhs'
LOCALE = 'zh_CN.utf8'

DATE_FORMATS = {
    'zhs': ((u'zh_CN', 'utf8'), u'%Y年%m月%d日(周%a)',),
}



DISQUS_SITENAME = 'silverchard'
DISQUS_DISPLAY_COUNTS = True
GOOGLE_ANALYTICS = 'UA-75935913-1'



TAG_FEED_ATOM = None
FEED_ATOM = None
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['static',
                'images',
                'uml',
                'images/favicon.ico',
                'static/CNAME']

EXTRA_PATH_METADATA = {
    'images/favicon.ico': {'path': 'favicon.ico'},
    'static/CNAME': {'path': 'CNAME'},
    'static/robots.txt': {'path': 'robots.txt'},
    'static/manifest.json': {'path': 'manifest.json'},
}

PAGE_URL = "{slug}.html"
PAGE_SAVE_AS = "{slug}.html"


PLUGIN_PATHS = ['plugins']
THEME = "theme"


I18N_SUBSITES = {
    'zhs': dict(
        LOCALE='zh_CN.utf8',
        SITENAME="Silver's Blog",
        STATIC_PATHS=STATIC_PATHS
    ),
}
# I18N_UNTRANSLATED_ARTICLES = "remove"

MD_EXTENSIONS = ['admonition',
                 'toc',
                 'codehilite(css_class=highlight,linenums=False)',
                 'extra']

PLUGINS = ["i18n_subsites",
           "better_codeblock_line_numbering",
           'tipue_search',
           'neighbors',
           'series',
           'bootstrapify',
           "render_math",
           'extract_toc',
           'tag_cloud',
           'sitemap',
           'summary']

SITEMAP = {
    'format': 'xml',
}

USE_LESS = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False
CHECK_MODIFIED_METHOD = "md5"
LOAD_CONTENT_CACHE = True
CACHE_CONTENT = True

# Theme options

# JINJA_EXTENSIONS = ['jinja2.ext.i18n']

DOCUTIL_CSS = True
TYPOGRIFY = False
PYGMENTS_STYLE = 'monokai'
GITHUB_USER = 'SilverChard'
GITHUB_SHOW_USER_LINK = True
DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True
CC_LICENSE = "CC-BY-NC-SA"
DISPLAY_TAGS_INLINE = True
OUTPUT_SOURCES = True
OUTPUT_SOURCES_EXTENSION = '.md'


DIRECT_TEMPLATES = (('search', 'index', 'categories', 'authors', 'archives',
                     'tags'))


AVATAR = 'images/avatar.jpg'
ABOUT_PAGE = "about.html"
ABOUT_ME = """<h3 style="text-align:center">
<a href="https://twitter.com/Silver_Chard"                  target="_blank">
<i class="fa fa-twitter" style="text-align:center"></i></a>
<a href="https://github.com/SilverChard"                   target="_blank">
<i class="fa fa-github" style="text-align:center"></i></a>
<a href="http://weibo.com/1843103547"                     target="_blank">
<i class="fa fa-weibo" style="text-align:center"></i></a>
<a href="https://www.facebook.com/ChardShieh"              target="_blank">
<i class="fa fa-facebook" style="text-align:center"></i></a>
<a href="https://plus.google.com/u/0/+SilverChard" target="_blank">
<i class="fa fa-google-plus" style="text-align:center"></i></a>
<a href="mailto:eva330680229@gmail.com" target="_blank">
<i class="mdi-communication-email" style="text-align:center"></i></a>
</h3>
"""
