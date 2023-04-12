# console.py
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

from gi.repository import Adw, Pango, Gtk, Vte, GLib
import os
import sys

@Gtk.Template(resource_path='/org/rhinolinux/system/gtk/console.ui')
class ConsoleView(Gtk.Box):
    __gtype_name__ = "ConsoleView"

    log_button: Gtk.Button = Gtk.Template.Child()
    log_box: Gtk.Box = Gtk.Template.Child()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Vte instance
        self.vte_instance = Vte.Terminal()
        self.vte_instance.set_cursor_blink_mode(Vte.CursorBlinkMode.ON)
        self.vte_instance.set_mouse_autohide(True)
        self.vte_instance.set_font(Pango.FontDescription("Source Code Pro Regular 12"))
        self.log_box.append(self.vte_instance)

    def on_show(self):
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
