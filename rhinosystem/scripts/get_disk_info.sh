#!/bin/sh
total_space_gb=$(echo "scale=2; $(df --output=size --total | awk 'END {print $1}') / 1000000" | bc)
if [ "$(echo "$total_space_gb > 1000" | bc -l)" != 0 ]; then
  printf "%.1f TB\n" "$(echo "scale=2; $total_space_gb / 1000" | bc)"
else
  printf "%.0f GB\n" "${total_space_gb}"
fi
