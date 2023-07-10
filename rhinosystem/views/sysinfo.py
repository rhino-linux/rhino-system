# sysinfo.py
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
from rhinosystem.widgets.inforow import Inforow
from rhinosystem.utils.deviceinfo import DeviceInfo
from rhinosystem.utils.threading import RunAsync

@Gtk.Template(resource_path='/org/rhinolinux/system/gtk/sysinfo.ui')
class SysinfoView(Gtk.Box):
    __gtype_name__ = "SysinfoView"

    board: Inforow = Gtk.Template.Child()
    chip: Inforow = Gtk.Template.Child()
    memory: Inforow = Gtk.Template.Child()
    disk: Inforow = Gtk.Template.Child()
    gpu: Inforow = Gtk.Template.Child()
    kernel: Inforow = Gtk.Template.Child()
    desktop: Inforow = Gtk.Template.Child()
    os: Inforow = Gtk.Template.Child()

    upgrade_button: Gtk.Button = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.board.set_title("Board")
        self.chip.set_title("Chip")
        self.memory.set_title("Memory")
        self.disk.set_title("Disk")
        self.gpu.set_title("GPU")
        self.kernel.set_title("Kernel")
        self.desktop.set_title("Desktop")
        self.os.set_title("OS")

        # Run these functions asynchronously since they can take a while to run (mainly cpu)
        RunAsync(self.set_system_info, None, self.board)
        RunAsync(self.set_system_info, None, self.chip)
        RunAsync(self.set_system_info, None, self.memory)
        RunAsync(self.set_system_info, None, self.disk)
        RunAsync(self.set_system_info, None, self.gpu)
        RunAsync(self.set_system_info, None, self.kernel)
        RunAsync(self.set_system_info, None, self.desktop)
        RunAsync(self.set_system_info, None, self.os)

    def set_system_info(self, widget):
        if widget == self.board:
            GLib.idle_add(self.board.set_label_text, DeviceInfo.get_board_info())
        elif widget == self.chip:
            GLib.idle_add(self.chip.set_label_text, DeviceInfo.get_cpu_info())
        elif widget == self.memory:
            GLib.idle_add(self.memory.set_label_text, DeviceInfo.get_memory_info())
        elif widget == self.disk:
            GLib.idle_add(self.disk.set_label_text, DeviceInfo.get_disk_info())
        elif widget == self.gpu:
            GLib.idle_add(self.gpu.set_label_text, DeviceInfo.get_gpu_info())
        elif widget == self.kernel:
            GLib.idle_add(self.kernel.set_label_text, DeviceInfo.get_kernel_info())
        elif widget == self.desktop:
            GLib.idle_add(self.desktop.set_label_text, DeviceInfo.get_desktop_info())
        elif widget == self.os:
            GLib.idle_add(self.os.set_label_text, DeviceInfo.get_os_info())