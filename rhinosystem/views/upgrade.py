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
import time
from rhinosystem.utils.threading import RunAsync
from rhinosystem.views.upgradepages.progressbar import ProgressView
from rhinosystem.views.upgradepages.console import ConsoleView

@Gtk.Template(resource_path='/org/rhinolinux/system/gtk/upgrade.ui')
class UpgradeView(Gtk.Box):
    __gtype_name__ = "UpgradeView"

    view_stack: Gtk.Stack = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.log=False
        self.window = None
        self.progress = ProgressView()
        self.console = ConsoleView()
        self.progress.show_log.connect("clicked", self.do_show_log)
        self.console.log_button.connect("clicked", self.do_show_log)
        self.view_stack.add_child(self.progress)
        self.view_stack.add_child(self.console)
        self.view_stack.set_visible_child(self.progress)


    def on_show(self, window):
        self.window = window
        self.progress.progress_bar.set_show_text(True)
        self.progress.progress_bar.set_text("Upgrading Rhino Linux")

        self.console.on_show()


    def do_show_log(self, widget):
        if self.log:
            self.view_stack.set_visible_child(self.progress)
            self.log = False
        else:
            self.view_stack.set_visible_child(self.console)
            self.log = True