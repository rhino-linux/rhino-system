#!/bin/bash
total_space=$(df --total --block-size=1K | grep total | awk '{print $2}')
total_space_gb=$(echo "scale=2; $total_space / 1000000" | bc)
if (( $(echo "$total_space_gb > 1000" | bc -l) )); then
  total_space_tb=$(echo "scale=2; $total_space_gb / 1000" | bc)
  printf "%.1f TB\n" "${total_space_tb}"
else
  printf "%.0f GB\n" "${total_space_gb}"
fi