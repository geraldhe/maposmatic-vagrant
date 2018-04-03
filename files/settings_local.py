#!/usr/bin/env python
# coding: utf-8

# maposmatic, the web front-end of the MapOSMatic city map generation system
# Copyright (C) 2009  David Decotigny
# Copyright (C) 2009  Frédéric Lehobey
# Copyright (C) 2009  David Mentré
# Copyright (C) 2009  Maxime Petazzoni
# Copyright (C) 2009  Thomas Petazzoni
# Copyright (C) 2009  Gaël Utard

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Copy this template into www/settings_local.py. Remove comment and edit
to your needs. You can add specific Django settings if needed:
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# # Contact email
CONTACT_EMAIL = "hartmut@php.net"

# # Make this unique, and don't share it with anybody.
SECRET_KEY = 'tm+wb)lp5q%br=p0d2toz&km_-w)cmcelv!7inons&^v9(q!d2'

# # If you want to provide extra information in the footer put it in EXTRA_FOOTER
# EXTRA_FOOTER = ""

# # Optional: if you need to extend the Python search path, for example to
# # include your OCitySMap installation, then write something like the
# # following:
# import sys
# sys.path.append('/path/to/ocitysmap')
# sys.path.append('/path/to/lib/python/site-packages')

# # Debug mode. Set to False on a production environnement
DEBUG = True

# # With DEBUG set to False error will be set to the following emails
ADMINS = (
    ('MapOSMatic admin', 'hartmut@php.net'),
)

# # By default an SQLite DB is set. It is only relevant for testing purpose.
# # You should use MySQL or PostgreSQL on production. Check Django doc:
# # https://docs.djangoproject.com/fr/1.10/ref/settings/#databases
# import os
# DATABASES = {
#     # For PostgreSQL:
#     'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': 'maposmatic',
#        'USER': 'maposmatic',
#        'PASSWORD': 'secret',
#        'HOST': 'localhost',
#        'PORT': '5432'
#        },
#
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'gis',
        'USER': 'maposmatic',
        'PASSWORD': 'secret',
        'HOST': 'gis-db',
        'PORT': '5432'
        },
}

# # Path to ocitysmap's config file to use, or None for the default
# # (~/.ocitysmap.conf)
OCITYSMAP_CFG_PATH = '/home/maposmatic/.ocitysmap.conf'

RENDERING_RESULT_PATH = '/home/maposmatic/maposmatic/rendering/results/'
RENDERING_RESULT_URL = '/results/' # Either a relative URL or an absolute URL
RENDERING_RESULT_FORMATS = ['png', 'svgz', 'pdf', 'csv']
RENDERING_RESULT_MAX_SIZE_GB = 10

# # Default output log file when env variable MAPOSMATIC_LOG_FILE is not set
DEFAULT_MAPOSMATIC_LOG_FILE = '/home/maposmatic/maposmatic/logs/maposmatic.log'

# # Default log level when the env variable DEFAULT_MAPOSMATIC_LOG_LEVEL
# # is not set
import logging
DEFAULT_MAPOSMATIC_LOG_LEVEL = logging.INFO
DEFAULT_MAPOSMATIC_LOG_FORMAT = "%(asctime)s - %(name)s@%(process)d - "\
                                "%(levelname)s - %(message)s"

# # Base bounding box
BASE_BOUNDING_BOX = (51.7, 7.5, 52.2, 9.5)


# # Maximum length of the bounding box to be rendered. This length is
# # checked in both directions (longitude and latitude).
# # Note: if you change this you should probably change
# # BBOX_MAXIMUM_LENGTH_IN_KM in osm_map.js too.
BBOX_MAXIMUM_LENGTH_IN_METERS = 20000

# # Number of items displayed per page in the jobs and maps pages
ITEMS_PER_PAGE = 25

# # PID file location for the rendering daemon associated with this
# # instance; normally managed by the /etc/init.d scripts such as
# # start-stop-daemon(8) in debian systems:
MAPOSMATIC_PID_FILE = '/var/run/maposmaticd.pid'

# Feed URL for the RRS feed on the front page
MAPOSMATIC_RSS_FEED = 'http://blog.osm-baustelle.de/index.php/feed/?cat=2'

# # Settings for exception emails: the from email address, and the list of
# # receipient email addresses. No emails are sent if the SMTP host is not
# # defined.
DAEMON_ERRORS_SMTP_HOST = None
DAEMON_ERRORS_SMTP_PORT = 25
DAEMON_ERRORS_EMAIL_FROM = 'daemon@domain.com'
DAEMON_ERRORS_EMAIL_REPLY_TO = 'noreply@domain.com'
DAEMON_ERRORS_JOB_URL = 'http://domain.com/jobs/%d'
DAEMON_ERRORS_SMTP_ENCRYPT = False
DAEMON_ERRORS_SMTP_USER = ''
DAEMON_ERRORS_SMTP_PASSWORD = ''

# # Show a link to donate to the MapOSMatic team
MAPOSMATIC_DONATION = False

# # Displayed on the top menu
BRAND_NAME = "MyOSMatic"
# # Front page feed
FRONT_PAGE_FEED = "https://blog.osm-baustelle.de/index.php/feed/"


# # Alert message (for instance for maintenance announce)
# ALERT_MESSAGE = ""

# # To respect the AGPL licence proper links to source code must be
# # displayed
MAPOSMATIC_FORK_URL = "https://github.com/hholzgra/maposmatic"
OCITYSMAP_FORK_URL = "https://githib.com/hholzgra/ocitysmap"

# root directory for uploaded files etc.
MEDIA_ROOT = '/home/maposmatic/maposmatic/media'

# we changed encoding of map titles in file names at some point, this is the
# last ID using the old scheme so that links to old files still work
# for fresh setups it can always be zero
LAST_OLD_ID = 0
