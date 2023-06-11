# deviceinfo.py
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
import os
import cpuinfo
import sys
import math
from rhinosystem.utils.command import Command
from rhinosystem.utils.log import setup_logging
logger=setup_logging()

class DeviceInfo:

    @staticmethod
    def get_cpu_info():
        info = cpuinfo.get_cpu_info()
        if info.get("vendor_id") == "AuthenticAMD":
            return info.get("vendor_id").replace(" with Radeon Graphics", "")
        return cpuinfo.get("vendor_id")

    @staticmethod
    def get_memory_info():
        out = Command.execute_command(
            command=[
                sys.path[1]+"/rhinosystem/scripts/get_memory.sh"
            ],
            command_description="Get memory info",
            crash=False,
        )
        if out[0] != 0:
            logger.error("Failed to get memory info")
            return "Failed to get memory info"

        return str(math.floor(int(out[1].decode("utf-8").strip())*0.001048576))+" GB"

    @staticmethod
    def get_gpu_info():
        out = Command.execute_command(
            command=[
                sys.path[1]+"/rhinosystem/scripts/get_gpu.sh"
            ],
            command_description="Get GPU info",
            crash=False,
        )
        if out[0] != 0:
            logger.error("Failed to get GPU info")
            return "Failed to get GPU info"
        return out[1].decode("utf-8").strip()

    @staticmethod
    def get_kernel_info():
        out = Command.execute_command(
            command=[
                "uname",
                "-r"
            ],
            command_description="Get kernel info",
            crash=False,
        )
        if out[0] != 0:
            logger.error("Failed to get kernel info")
            return "Failed to get kernel info"
        return out[1].decode("utf-8").strip()

    @staticmethod
    def get_os_info():
        with open("/etc/os-release", "r") as f:
            for line in f:
                if line.startswith("PRETTY_NAME"):
                    return line.split("=")[1].replace('"', "").strip()

    @staticmethod
    def get_os_version():
        with open("/etc/os-release", "r") as f:
            for line in f:
                if line.startswith("VERSION_ID"):
                    return line.split("=")[1].replace('"', "").strip()
        return "Unknown"

    @staticmethod
    def get_desktop_info():
        desktop = os.environ.get("XDG_CURRENT_DESKTOP", "Unknown")
        if desktop == "Unknown":
            return "Unknown"
        else:
            return desktop.replace("X-", "").replace("Budgie:GNOME", "Budgie").replace(":Unity7:ubuntu", "")
