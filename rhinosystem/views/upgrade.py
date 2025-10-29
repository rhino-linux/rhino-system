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
from gi.repository import Gio
from gi.repository import Gdk
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
        self.vte_instance.set_mouse_autohide(False)
        self.vte_instance.set_font(Pango.FontDescription("Monospace 10"))
        self.vte_instance.set_cursor_shape(Vte.CursorShape.IBEAM)

        # Enable copy/paste functionality
        self.vte_instance.set_allow_hyperlink(True)
        # Enable default copy/paste shortcuts (Ctrl+Shift+C/V)
        self.vte_instance.set_input_enabled(True)

        # Connect right-click context menu
        gesture = Gtk.GestureClick.new()
        gesture.set_button(3)  # Right mouse button
        gesture.connect("pressed", self.on_right_click)
        self.vte_instance.add_controller(gesture)

        # Add keyboard shortcuts for copy/paste
        key_controller = Gtk.EventControllerKey.new()
        key_controller.connect("key-pressed", self.on_key_pressed)
        self.vte_instance.add_controller(key_controller)

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

    def on_right_click(self, gesture, n_press, x, y):
        """Handle right-click to show context menu"""
        menu = Gio.Menu.new()

        # Add Copy action
        copy_action = Gio.MenuItem.new("Copy", "terminal.copy")
        menu.append_item(copy_action)

        # Create popover menu
        popover = Gtk.PopoverMenu.new_from_model(menu)
        popover.set_parent(self.vte_instance)
        popover.set_position(Gtk.PositionType.BOTTOM)

        # Set pointing position (use widget coordinates)
        rect = Gdk.Rectangle()
        rect.x = int(x)
        rect.y = int(y)
        rect.width = 1
        rect.height = 1
        popover.set_pointing_to(rect)

        # Connect actions
        action_group = Gio.SimpleActionGroup.new()
        copy_simple_action = Gio.SimpleAction.new("copy", None)
        copy_simple_action.connect("activate", lambda action, param: self.vte_instance.copy_clipboard())
        action_group.add_action(copy_simple_action)

        self.vte_instance.insert_action_group("terminal", action_group)
        popover.popup()

    def on_key_pressed(self, controller, keyval, keycode, state):
        """Handle keyboard shortcuts for copy"""
        # Check for Ctrl+Shift+C (copy)
        if (state & Gdk.ModifierType.CONTROL_MASK) and (state & Gdk.ModifierType.SHIFT_MASK):
            if keyval == Gdk.KEY_C or keyval == Gdk.KEY_c:
                self.vte_instance.copy_clipboard()
                return True
        return False

    def on_finish(self, *args):
#        self.upgradeRunningBox.set_visible(False)
        self.upgradeCompleteBox.set_visible(True)
        self.window.title.set_label("Update Complete")
    
    def quit(self, *args):
        sys.exit(0)
