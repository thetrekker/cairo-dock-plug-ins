/*
** Login : <ctaf42@gmail.com>
** Started on  Fri Nov 30 05:31:31 2007 GESTES Cedric
** $Id$
**
** Copyright (C) 2007 GESTES Cedric
** This program is free software; you can redistribute it and/or modify
** it under the terms of the GNU General Public License as published by
** the Free Software Foundation; either version 3 of the License, or
** (at your option) any later version.
**
** This program is distributed in the hope that it will be useful,
** but WITHOUT ANY WARRANTY; without even the implied warranty of
** MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
** GNU General Public License for more details.
**
** You should have received a copy of the GNU General Public License
** along with this program; if not, write to the Free Software
** Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
*/

#include "stdlib.h"

#include "systray-config.h"
#include "systray-menu-functions.h"
#include "systray-init.h"
#include "cd-tray.h"
#include "systray-struct.h"

AppletConfig myConfig;
AppletData myData;

CD_APPLET_DEFINITION ("systray", 1, 4, 7)


CD_APPLET_INIT_BEGIN (erreur);
{
  CD_APPLET_REGISTER_FOR_CLICK_EVENT;
  CD_APPLET_REGISTER_FOR_MIDDLE_CLICK_EVENT;
  CD_APPLET_REGISTER_FOR_BUILD_MENU_EVENT;
  systray_apply_settings();
}
CD_APPLET_INIT_END


CD_APPLET_STOP_BEGIN
{
  CD_APPLET_UNREGISTER_FOR_CLICK_EVENT;
  CD_APPLET_UNREGISTER_FOR_MIDDLE_CLICK_EVENT;
  CD_APPLET_UNREGISTER_FOR_BUILD_MENU_EVENT;

  //\_________________ On libere toutes nos ressources.
  reset_config ();
  reset_data ();
}
CD_APPLET_STOP_END


CD_APPLET_RELOAD_BEGIN
{
  if (CD_APPLET_MY_CONFIG_CHANGED)
    systray_apply_settings();
}
CD_APPLET_RELOAD_END
