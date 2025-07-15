#!/bin/bash

unset ccount sorted joined output
declare -A ccount

while IFS= read -r model; do
  ((ccount["${model}"]++))
done < <(lscpu -e=modelname | tail -n +2 | sed -e 's/with Radeon Graphics//g' -e 's/(R) Core(TM)//g')

mapfile -t sorted < <(printf '%s\n' "${!ccount[@]}" | sort)
for i in "${sorted[@]}"; do
  joined+=("${ccount[$i]} x ${i}")
done

printf -v output '%s + ' "${joined[@]}"
echo "${output% + }"

# will print result like `4x Cortex-A55` or `4x Cortex-A53 + 2x Cortex-A72` or `24 x 13th Gen Intel i7-13700K`
