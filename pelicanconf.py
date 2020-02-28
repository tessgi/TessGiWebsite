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
TWITTER_USERNAME = "NASA_TESS"

HIDE_SIDEBAR = True

if pelican.__version__ >= '3.7.0':
    MARKDOWN = {
        'extension_configs': {
            'markdown.extensions.toc': {},
            'markdown.extensions.tables': {},
        },
    }
else:
    MD_EXTENSIONS = (['toc'])


# Which static data dirs should be uploaded as part of the website?
STATIC_PATHS = (['images', 'data', 'docs'])

# Directories that contain html files we want to exclude
# because they are sub-pages included through rst includes
PAGE_EXCLUDES = ['pages/observing/approved-programs']

# The fancy table of contents sidebar requires a plugin
PLUGIN_PATHS = [os.path.join(os.path.dirname(os.path.realpath(__file__)),
                             "plugins")]
PLUGINS = ['extract_toc']

# Defines the menu items in the top bar
MENUITEMS = (
        ('News', 'archives.html'),
        ('Mission', (
            ('Objectives', 'objectives.html'),
            ('Telescope', 'the-tess-space-telescope.html'),
            ('Operations', 'operations.html'),
            ('Science', 'primary-science.html'),
            ('Publications', 'publications.html'),
            # ('Conferences', 'conferences.html'),
            # ('Users Panel', 'users-panel.html'),
            )
         ),
        ('Using TESS', (
            ('Observing dates', 'status.html'),
            ('Guest Investigator Program', 'proposing-investigations.html'),
            ('Technical details', 'observing-technical.html'),
            # ('Campaign fields', 'k2-fields.html'),
            # ('Data release notes', 'k2-data-release-notes.html'),
            ('Proposal tools', 'proposal-tools.html'),
            ('Approved programs', 'approved-programs.html'),
            #('Discretionary targets', 'ddt.html'),
            #('FAQ', 'faq.html'),
            # ('C9 Microlensing experiment', 'k2-c9.html'),
            # ('C16 Supernova experiment', 'supernova-experiment'),
            )
         ),
        ('Data analysis', (
            ('Data access', 'data-access.html'),
            #('Follow-up program', 'followup.html'),
            ('Analysis software', 'software.html'),
            #('Pipeline', 'pipeline.html'),
            ('Community products', 'community.html'),
            ('Documentation', 'documentation.html'),
            )
         ),
        ('Education & Outreach', (
            ('Resources', 'gallery.html'),
            ('Media support', 'media.html'),
            )
         ),            
        ('FAQ', 'faq.html'),
        ('HEASARC', 'https://heasarc.gsfc.nasa.gov')
        )

# Defines the "key information" box on the front page
KEY_INFORMATION = (
    # ('Proposal submission page', 'https://heasarc.gsfc.nasa.gov/ark/rps/'),
    ('Web TESS Target Tool', 'https://heasarc.gsfc.nasa.gov/cgi-bin/tess/webtess/wtv.py'),
    #('Observatory Guide', 'documentation.html'),
    ('Observing dates', 'https://heasarc.gsfc.nasa.gov/docs/tess/status.html'),
    ('Data at MAST', 'http://archive.stsci.edu/tess/summary.html'),    
    ('Frequently asked questions', 'faq.html'),
    ('Volunteer to serve on a review panel',
        'https://goo.gl/forms/p4ZqiTQSEHjbM6nz2'),
    ('Do you have a news-worthy TESS result?', 'media.html'),
    ('Contact us', 'helpdesk.html'),
    # ('Cycle 1 Proposal submission',
    #     '[https://heasarc.gsfc.nasa.gov/ark/rps/'),
    # ('Simulated data', 'data-access.html#simulated-data'),
) # make the simulated data link work!

# Defines the "important dates" box on the front page
IMPORTANT_DATES = (
            # ('<b>6 Oct 2017</b>',
            #  'Cycle 1 proposal submission deadline ',
            #  'proposing-investigations.html'), # link to a new item?
            #('<b>April 18 2018</b>',
            # 'TESS launch',
            # 'operations.html'), # link to a news item?
            # ('<b>December 6, 2018</b>',
            #  'Sector 1 and 2 data release',
            #  'status.html'), # link to a news item?
            # ('<b>January 25, 2019</b>',
            #  'Sector 3 and 4 data release',
            #  'status.html'), # link to a news item?
            # ('<b>16 January 2020</b>',
            #  'Cycle 3 proposals due',
            #  'proposing_investigations.html',), # link to a news item?
            ('<b>5 July 2020</b>',
             'Cycle 3 observations begin',
             'status.html',), # link to a news item?
         )

# Defines the "meetings" box on the front page
MEETINGS = (
            # ('<b>4–8 Jun 2017</b><br>'
            #  'AAS 230th Meeting',
            #  'tess-community-science-center-team-at-aas-230.html'),
            # ('<b>19–23 Jun 2017</b><br>'
            #  'Kepler & K2 SciCon IV',
            #  'https://keplerscience.arc.nasa.gov/scicon4/'),
            # ('<b>16-21 July 2017</b><br>'
            #  'Tessting Stellar Astrophysics, TASC3 KASC10 Workshop',
            #  'http://www.tasc3kasc10.com/'),
            # ('<b>17-21 July 2017</b><br>'
            #  'Transiting Exoplanets',
            #  'https://wasp-planets.net/conference/'),
            # ('<b>9-12 October 2017</b><br>'
            #  'Know Thy Star, Know Thy Planet - Assessing the Impact of Stellar Characterization on Our Understanding of Exoplanets',
            #  'http://nexsci.caltech.edu/conferences/2017/knowthystar/'),
            # ('<b>15-20 October 2017</b><br>'
            #  '49th Meeting of the AAS Division for Planetary Sciences',
            #  'https://aas.org/meetings/dps49'),
            # ('<b>26-27 October 2017</b><br>'
            #  'BDEXOCON-2017: Brown Dwarf to Exoplanet Connection',
            #  'https://bdexocon.wordpress.com/'),
            # ('<b>13-17 November 2017</b><br>'
            #  'IAUS 339: Southern Horizons in Time­ Domain Astronomy',
            #  'https://www.hou.usra.edu/meetings/habitableworlds2017/'),
            # ('<b>13-17 November 2017</b><br>'
            #  'Habitable Worlds 2017:  A System Science Workshop',
            #  'http://nexsci.caltech.edu/conferences/2017/knowthystar/'),
            # ('<b>8-12 January 2018</b><br>'
            #  '231st Meeting of the American Astronomical Society',
            #  'https://aas.org/meetings/aas231'),
            #('<b>5-9 March 2018</b><br>'
            # 'Preparing for TESS',
            # 'http://tess.ninja/'),
            # ('<b>3-7 June 2018</b><br>'
            #  '232nd Meeting of the American Astronomical Society',
            #  'https://aas.org/meetings/aas232'),            
            # ('<b>2-6 July 2018</b><br>'
            #  'Exoplanets II',
            #  'https://www.exoplanetscience2.org'),
            # ('<b>8-13 July 2018</b><br>'
            #  'TASC4/KASC11',
            #  'https://tasoc.dk'),
            # ('<b>14-22 July 2018</b><br>'
            #  'COSPAR',
            #  'http://cospar2018.org'),
            # ('<b>29 July - 3 Aug 2018</b><br>'
            #  'Cool Stars 20', 
            #  'http://coolstars20.cfa.harvard.edu'),       
            #('<b>20-31 August 2018</b><br>'
            # 'International Astronomical Union',
            # 'https://astronomy2018.univie.ac.at'),
            # ('<b>6-10 January 2019</b><br>'
            #  'AAS Winter Meeting',
            #  'https://aas.org/meetings/aas233'),           
            #('<b>11-14 February 2019</b><br>'
            # 'TESS Data Workshop',
            # 'http://www.stsci.edu/institute/conference/tess'),               
            # ('<b>4-8 March 2019</b><br>'
            #  'Kepler Science Conference',
            #  'https://keplerscience.arc.nasa.gov/scicon-2019/index.html'),           
            # ('<b>25-29 March 2019</b><br>'
            #  'Building Early Science with TESS',
            #  'http://tess.ninja/'),   
            # ('<b>15 April - 28 June 2019</b><br>'
            #  'Better Stars, Better Planets: Exploiting the Stellar-Exoplanetary Synergy',
            #  'https://www.kitp.ucsb.edu/activities/exostar19'),
            #('<b>22-26 July 2019</b><br>'
            # 'TASC5/KASC12 Workshop',
            # 'http://web.mit.edu/tasc5/index.html'),    
            #('<b>29 July - 2 August 2019</b><br>'
            # 'TESS Science Conference',
            # 'https://tess.mit.edu/news/tess-science-conference/'),
            #('<b>4-8 November 2019</b><br>'
            # 'SEEC Symposium: Rocky Exoplanets in the Era of JWST: Theory and Observation',
            # 'https://seec.gsfc.nasa.gov/Symposium.html'),
            ('<b>4-8 January 2020</b><br>'
             'AAS Winter Meeting',
             'https://aas.org/meetings/aas235'),
            ('<b>10-14 February 2020</b><br>'
             'Expanding the Science of TESS',
             'https://tess.ninja/three/')
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
