#!/bin/sh
case $(dpkg --print-architecture) in
amd64)
  if [ -f "/sys/devices/virtual/dmi/id/board_name" ]; then
    vendor=$(tr -d '\0' < /sys/devices/virtual/dmi/id/sys_vendor)
    case $(tr -d '\0' < /sys/devices/virtual/dmi/id/board_name) in 
      *\(*\)*) 
        board_name="$(tr -d '\0' < /sys/devices/virtual/dmi/id/board_name | sed -n 's/.*\(([^()]*)\).*/\1/p' | tr -d '()')"
        ;;
      *)
        board_name="$(tr -d '\0' < /sys/devices/virtual/dmi/id/board_name)"
        ;;
    esac
    board="${vendor} ${board_name}"
  else
    board="Unknown"
  fi
  ;;
arm64)
  if [ -f "/proc/device-tree/model" ]; then
    board="$(tr -d '\0' < /proc/device-tree/model)"
  else
    board="Unknown"
  fi
  ;;
esac
echo "${board}"
