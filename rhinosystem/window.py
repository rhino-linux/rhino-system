# window.py
#
# Copyright 2023 axtlos <axtlos@getcryst.al>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License only
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-only

from gi.repository import Adw, Gtk, Gdk, GLib
from os import system
import time
from rhinosystem.views.sysinfo import SysinfoView
from rhinosystem.views.upgrade import UpgradeView
from rhinosystem.widgets.inforow import Inforow
from rhinosystem.utils.deviceinfo import DeviceInfo
from rhinosystem.utils.threading import RunAsync

@Gtk.Template(resource_path='/org/rhinolinux/system/window.ui')
class RhinosystemWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'RhinosystemWindow'

    stack_view: Gtk.Stack = Gtk.Template.Child()
    version: Gtk.Button = Gtk.Template.Child()
    version_invalid: Gtk.Button = Gtk.Template.Child()
    title: Gtk.Label = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.os_info = SysinfoView()
        self.upgrade_progress = UpgradeView()
        self.version.connect("clicked", self.copy_version)
        self.os_info.upgrade_button.connect("clicked", self.upgrade_os)
        self.stack_view.add_child(self.os_info)
        self.stack_view.add_child(self.upgrade_progress)
        if DeviceInfo().get_os_version() != "Unknown":
            validation: float = float(DeviceInfo().get_os_version())
            self.version_invalid.set_visible(False)
            self.version.set_label(DeviceInfo().get_os_version())
        else: self.version.set_visible(False)

    def upgrade_os(self, widget):
        self.os_info.set_visible(False)
        self.upgrade_progress.set_visible(True)
        self.upgrade_progress.on_show(self)
        self.title.set_label("Updating Rhino Linux")

    def copy_version(self, widget):
        system(f"echo -n \"{DeviceInfo().get_os_version()}\" | xclip -selection c")
