#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import datetime
import pelican

# If `DEVMODE = True`, show a red warning banner at the top
DEVMODE = False   # pelicanconf-dev.py will override this

# By default, use agressive caching.
# The Makefile ensures we use `--ignore-cache` for production builds.
CACHE_CONTENT = True
LOAD_CONTENT_CACHE = True
CHECK_MODIFIED_METHOD = 'mtime'
CONTENT_CACHING_LAYER = 'generator'  # This causes an empty news page
WITH_FUTURE_DATES = False

ANALYTICS = ()   # pelicanconf-live.py will override this

AUTHOR = u'Thomas Barclay'
SITENAME = "TESS"
BANNER_SUBTITLE = "Science Support Center"
SITEURL = "https://heasarc.gsfc.nasa.gov/docs/tess"
FULLURL = "https://heasarc.gsfc.nasa.gov/docs/tess"
SITELOGO = 'images/NASA_logo_vector_lg.png'
SITELOGO_SIZE = 32
FAVICON = 'images/favicon.png'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = u'en'

PATH = 'content'
THEME = "themes/pelican-bootstrap3-kepler"
BOOTSTRAP_THEME = 'cosmo'
BOOTSTRAP_FLUID = False

BANNER = "images/tess-banner-inverted_v2.jpg"
HIDE_SITENAME = False

IGNORE_FILES = [
    "README.md",
]

# Enable RSS feeds
# FEED_DOMAIN = "https://keplerscience.arc.nasa.gov"
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = "feeds/all.atom.xml"
FEED_ALL_RSS = "feeds/all.rss.xml"
# We don't need per-author or per-category or per-translation feeds
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_BREADCRUMBS = False
OPEN_GRAPH_IMAGE = "images/logo-for-twitter.jpeg"
TWITTER_CARDS = False
TWITTER_USERNAME = "tesshelp"

HIDE_SIDEBAR = True

if pelican.__version__ >= '3.7.0':
    MARKDOWN = {
        'extension_configs': {
            'markdown.extensions.toc': {},
            'markdown.extensions.tables': {},
        },
        'extensions': ['mdx_include']
    }
else:
    MD_EXTENSIONS = (['toc'])


# Which static data dirs should be uploaded as part of the website?
STATIC_PATHS = (['images', 'data', 'docs'])

# Directories that contain html files we want to exclude
# because they are sub-pages included through rst includes
PAGE_EXCLUDES = ['pages/observing/approved-programs', ]

# The fancy table of contents sidebar requires a plugin
PLUGIN_PATHS = [os.path.join(os.path.dirname(os.path.realpath(__file__)),
                             "plugins")]
PLUGINS = ['extract_toc']

# Defines the menu items in the top bar
MENUITEMS = (
        ('Mission', (
            ('Objectives', 'objectives.html'),
            ('Telescope', 'the-tess-space-telescope.html'),
            ('Primary mission', 'primary.html'),
            ('First Extended mission', 'extended.html'),
            ('Second Extended mission', 'second-extended.html'),
            ('FAQ', 'faq.html'),
            ('Citizen Science', 'citizenscience.html'),
            ('Outreach resources', 'gallery.html'),
            ('Publications', 'publications.html'),
            ('Media Request', 'media.html'),
                    )
        ),
        ('Data & tools', (
            ('Data pipeline', 'data-handling.html'),
            ('Data products', 'data-products.html'),
            ('Data access', 'data-access.html'),
            ('Data analysis tools', 'data-analysis-tools.html'),
            ('Community products', 'community.html'),
            ('Community tools', 'community-tools.html'),
            ('Documentation', 'documentation.html'),
            ('Data release notes', 'data_release_notes.html'),
                      )
        ),
        ('Observations', (
          #  ('TESS at a glance', 'quicklook-mission.html'),
            ('Technical details', 'observing-technical.html'),
            ('Sector dates', 'sector.html'),
            ('Approved GI programs', 'approved-programs.html'),
                         )
        ),
        ('Proposing', (
            ('Guest Investigator Proposals', 'proposing-investigations.html'),
            ('Proposal & observation tools', 'proposal-tools.html'),
            ("Director's Discretionary Target program", 'ddt.html'),
            ('Proposal templates', 'proposal-templates.html'),
                      )
        ),
        # ('Education & Outreach', (
        #     ('Resources', 'gallery.html'),
        #     ('Media support', 'media.html'),
        #                          )
        # ),
        #
        )

# Defines the "key information" box on the front page
KEY_INFORMATION = (
    ('The TESS extended mission', 'extended.html'),
    ('Telescope Information', 'the-tess-space-telescope.html'),
    ('How to access the data', 'data-access.html'),
    ('Web TESS Target Tool', 'https://heasarc.gsfc.nasa.gov/cgi-bin/tess/webtess/wtv.py'),
    ('Observing dates', 'sector.html'),
    ('Proposing science', 'proposing-investigations.html'),
    ('Citizen Science projects', 'citizenscience.html'),
    ('Volunteer to serve on a review','https://goo.gl/forms/p4ZqiTQSEHjbM6nz2'),
    ('Do you have a news-worthy TESS result?', 'media.html'),
    ('Outreach Resources', 'gallery.html'),
    ('Publications', 'publications.html'),
    )


# Defines the "important dates" box on the front page
IMPORTANT_DATES = (
    ('<b>8th January 2023</b>',
             'AAS #241 Workshop: NASAs TESS Mission Interactive Data Workshop',
             '',),
     )

# Defines the "meetings" box on the front page
MEETINGS = (
    ('<b>8th - 12th January 2023</b>',
     'AAS #241',
            'https://aas.org/meetings/aas241',),
    ('<b>12th - 16th December 2022</b>',
     'AGU Fall Metting',
            'https://www.agu.org/Fall-Meeting',),
            )

# Defines the "related websites" listing in the footer of all pages
RELATEDSITES = (
            ('News, Media, and Education Resources',
             'https://nasa.gov/tess'),
            ('TESS @ MIT',
             'http://tess.mit.edu/'),
            # ('TESS @ Orbital ATK',
            #  'http://www.ballaerospace.com/page.jsp?page=72'),
            ('TESS @ MAST',
             'http://archive.stsci.edu/tess'),
            ('High Energy Astrophysics Science Archive Research Center',
             'https://heasarc.gsfc.nasa.gov/'),
            ('NASA Exoplanet Archive @ IPAC',
             'http://exoplanetarchive.ipac.caltech.edu'),
            )

SHOW_ARTICLE_AUTHOR = True
DEFAULT_PAGINATION = 5

RELATIVE_URLS = True

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

BOOTSTRAP_NAVBAR_INVERSE = True


DATE_MODIFIED = datetime.datetime.now().strftime('%Y-%m-%d')
