#
# Project Ginger S390x
#
# Copyright IBM, Corp. 2015
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 USA

import gettext

_ = gettext.gettext


messages = {
    "GS390XINVTYPE": _("Only supported type: '%(supported_type)s'."),
    "GS390XINVINPUT": _("Invalid input. Reason =  %(reason)s"),
    "GS390XCMD0001E": _("Command failed. Command = %(command)s, RC = %(rc)s, "
                        "REASON = %(reason)s'."),
    "GS390XREG0001E": _("Issue with regex. Reason =  %(reason)s"),

    "GS390XIOST001E": _("Failed to bring device online. Error = %(error)s"),
    "GS390XIOST002E": _("Failed to add dasd-eckd device in dasd.conf file. Device = %(device)s"),
    "GS390XIOST003E": _("Failed to remove device from dasd.conf file. Device = %(device)s"),

    "GS390XIONW001E": _("Failed to bring network device %(device)s online. Error = %(error)s"),
    "GS390XIONW002E": _("Failed to persist network device %(device)s in "
                        "ifcfg file %(ifcfg_file_path)s. Error = %(error)s"),
    "GS390XIONW003E": _("Failed to bring network device %(device)s offline. Error = %(error)s"),
    "GS390XIONW004E": _("Failed to remove ifcfg file %(ifcfg_file_path)s of network "
                        "device %(device)s. Error = %(error)s"),
    "GS390XIONW005E": _("Failed to create ifcfg file %(ifcfg_file_path)s for "
                        "network device %(device)s. Error = %(error)s"),

    "GS390XIOIG001E": _("Failed to retrieve devices in ignored list = %(error)s"),
    "GS390XIOIG002E": _("Failed to remove devices from ignore list. "
                        "Failed Devices = %(failed_devices)s")
}
