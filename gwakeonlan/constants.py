##
#     Project: gWakeOnLAN
# Description: Wake up your machines using Wake on LAN
#      Author: Fabio Castelli (Muflone) <webreg@vbsimple.net>
#   Copyright: 2009-2013 Fabio Castelli
#     License: GPL-2+
#  This program is free software; you can redistribute it and/or modify it
#  under the terms of the GNU General Public License as published by the Free
#  Software Foundation; either version 2 of the License, or (at your option)
#  any later version.
#
#  This program is distributed in the hope that it will be useful, but WITHOUT
#  ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
#  FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
#  more details.
#  You should have received a copy of the GNU General Public License along
#  with this program; if not, write to the Free Software Foundation, Inc.,
#  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA
##

import sys
import os.path

# Application constants
APP_NAME = 'gWakeOnLAN'
APP_VERSION = '0.6'
APP_DESCRIPTION = 'Wake up your machines using Wake on LAN.'
APP_ID = 'gwakeonlan.muflone.com'
APP_URL = 'http://gwakeonlan.muflone.com/'
APP_AUTHOR = 'Fabio Castelli'
APP_AUTHOR_EMAIL = 'webreg@vbsimple.net'
APP_COPYRIGHT = 'Copyright 2009-2013 %s' % APP_AUTHOR
# Other files
ARP_CACHE_FILENAME = '/proc/net/arp'
BROADCAST_ADDRESS = '255.255.255.255'
DOMAIN_NAME = 'gwakeonlan'

# If there's a file data/gwakeonlan.png then the shared data are searched in
# relative paths, else the standard paths are used
if os.path.isfile(os.path.join('data', 'gwakeonlan.png')):
  DIR_PREFIX = '.'
  DIR_LOCALE = os.path.join(DIR_PREFIX, 'locale')
else:
  DIR_PREFIX = os.path.join(sys.prefix, 'share', 'gwakeonlan')
  DIR_LOCALE = os.path.join(sys.prefix, 'share', 'locale')
# Set the paths for the folders
DIR_DATA = os.path.join(DIR_PREFIX, 'data')
DIR_UI = os.path.join(DIR_PREFIX, 'ui')
# Set the paths for the UI files
UI_MAIN = os.path.join(DIR_UI, 'main.glade')
UI_DETAIL = os.path.join(DIR_UI, 'detail.glade')
UI_ARPCACHE = os.path.join(DIR_UI, 'arpcache.glade')
UI_ABOUT = os.path.join(DIR_UI, 'about.glade')
UI_APPMENU = os.path.join(DIR_UI, 'appmenu.ui')
# Set the paths for the data files
DATA_ICON = os.path.join(DIR_DATA, 'gwakeonlan.png')
# Verbose level
VERBOSE_LEVEL_QUIET = 0
VERBOSE_LEVEL_NORMAL = 1
VERBOSE_LEVEL_MAX = 2