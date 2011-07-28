# This is a part of the Cairo-Dock plug-ins.
# Copyright : (C) 2010-2011 by Fabounet
# E-mail : fabounet@glx-dock.org
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# http://www.gnu.org/licenses/licenses.html#GPL

# Base class for Cairo-Dock's main interface.

####################
### dependancies ###
####################
import os.path
import dbus
import re

USER_CONFIG_DIR = os.path.abspath("~/.config")


##################
### Main class ###
##################
class CairoDock:
	
	#############
	### Enums ###
	#############
	# orientation
	BOTTOM = 0
	TOP    = 1
	RIGHT  = 2
	LEFT   = 3
	# container type
	DOCK    = "Dock"
	DESKLET = "Desklet"
	# emblem position
	UPPER_LEFT  = 0
	LOWER_RIGHT = 1
	LOWER_LEFT  = 2
	UPPER_RIGHT = 3
	MIDDLE      = 4
	# module category
	CATEGORY_BEHAVIOR         = 0
	CATEGORY_THEME            = 1
	CATEGORY_APPLET_FILES     = 2
	CATEGORY_APPLET_INTERNET  = 3
	CATEGORY_APPLET_DESKTOP   = 4
	CATEGORY_APPLET_ACCESSORY = 5
	CATEGORY_APPLET_SYSTEM    = 6
	CATEGORY_APPLET_FUN       = 7
	# module type
	CAN_DOCK    = 1
	CAN_DESKLET = 2
	# icon type
	TYPE_LAUNCHER        = "Launcher"
	TYPE_APPLICATION     = "Application"
	TYPE_APPLET          = "Applet"
	TYPE_SEPARATOR       = "Separator"
	TYPE_CONTAINER       = "Container"
	TYPE_CLASS_CONTAINER = "Class-Container"
	TYPE_OTHER           = "Other"
	# toggle dock visibility
	HIDE_DOCK   = 0
	SHOW_DOCK   = 1
	TOGGLE_DOCK = 2
	
	#####################
	### INIT AND DBUS ###
	#####################
	
	def __init__(self, app_name="cairo-dock"):
		""" Initialize the interface.
		It defines the following:
		 - cDataDir: main dir
		 - cCurrentThemeDir: current theme dir
		 - cConfFile : path to the global config file
		 """
		self.dock = None
		self.cAppName = app_name
		self.cDataDir = USER_CONFIG_DIR + '/' + app_name
		self.cCurrentThemeDir = self.cDataDir + '/current_theme'
		self.cLaunchersDir = self.cCurrentThemeDir + '/launchers'
		self.cPluginsDir = self.cCurrentThemeDir + '/plug-ins'
		self.cConfFile = self.cCurrentThemeDir + '/' + app_name + '.conf'
		
		self._connect()
	
	def _connect(self):
		# get gldi on the bus.
		bus = dbus.SessionBus()
		
		name1 = self.cAppName.replace('-','')  # -> cairodock
		name2 = re.sub('-[a-z]', lambda x: x.group(0).upper(), self.cAppName)
		name2 = re.sub('^[a-z]', lambda x: x.group(0).upper(), name2)  # -> CairoDock
		name2 = name2.replace('-','')  # -> CairoDock
		cBusPath = '/org/'+name1+'/'+name2
		try:
			dbus_object = bus.get_object("org.cairodock.CairoDock", cBusPath)
		except:
			print ">>> object '"+cBusPath+"' can't be found on the bus, exit.\nMake sure that Cairo-Dock is running"
			return
		self.iface = dbus.Interface(dbus_object, "org.cairodock.CairoDock")  # this object represents gldi.
		
