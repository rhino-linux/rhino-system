# command.py
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

import subprocess
import os
import sys
from rhinosystem.utils.log import setup_logging
logger=setup_logging()

class Command:
    @staticmethod
    def execute_command(
        command: list,
        command_description: str = "",
        crash: bool = False,
        workdir: str = "",
    ) -> [str, str, str]:
        if os.environ.get("DEBUG"):
            logger.debug("Command: " + " ".join(command))
            if os.environ.get("SHARDS_FAKE"):
                return [0, "", ""]

        out = subprocess.run(
            command,
            #shell=True,
            capture_output=True,
            cwd=workdir if workdir.strip() != "" else None
        )
        if out.returncode != 0 and command_description.strip() != "":
            logger.error(command_description+" failed with returncode "+str(out.returncode))
            if crash:
                sys.exit(out.returncode)
        elif out.returncode != 0:
            logger.error(" ".join(command)+" failed with returncode "+str(out.returncode))
            if crash:
                sys.exit(out.returncode)

        return [out.returncode, out.stdout, out.stderr]