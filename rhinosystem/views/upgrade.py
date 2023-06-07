# upgrade.py
#
# Copyright 2023 axtlos <axtlos@getcryst.al>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License only.
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

from gi.repository import Adw
from gi.repository import Gtk
from gi.repository import GLib
from gi.repository import Vte
from gi.repository import Pango
import time, sys
from rhinosystem.utils.threading import RunAsync

@Gtk.Template(resource_path='/org/rhinolinux/system/gtk/upgrade.ui')
class UpgradeView(Gtk.Box):
    __gtype_name__ = "UpgradeView"

    log_box: Gtk.Box = Gtk.Template.Child()
    upgradeRunningBox: Gtk.Box = Gtk.Template.Child()
    upgradeCompleteBox: Gtk.Box = Gtk.Template.Child()
    quitButton: Gtk.Button = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.log=False
        self.window = None
        self.vte_instance = Vte.Terminal()
        self.vte_instance.set_cursor_blink_mode(Vte.CursorBlinkMode.ON)
        self.vte_instance.set_mouse_autohide(True)
        self.vte_instance.set_font(Pango.FontDescription("Source Code Pro Regular 12"))
        self.log_box.append(self.vte_instance)
        self.quitButton.connect('clicked', self.quit)

    def on_show(self, window):
        self.window = window
        self.vte_instance.spawn_async(
            Vte.PtyFlags.DEFAULT,
            ".",  # working directory
            ["rpk", "update", "-y"],
            [],  # environment
            GLib.SpawnFlags.DO_NOT_REAP_CHILD,
            None,
            None,
            -1,
            None,
            None,
        )
        self.vte_instance.connect('child-exited', self.on_finish)

    def on_finish(self, *args):
#        self.upgradeRunningBox.set_visible(False)
        self.upgradeCompleteBox.set_visible(True)
        self.window.title.set_label("Update Finished")
    
    def quit(self, *args):
        sys.exit(0)
