#!/bin/bash
mapfile -t core < <(lscpu | grep 'Model name' | awk '{print $3}')
mapfile -t count < <(lscpu | grep 'per socket\|per cluster' | awk '{print $4}')

amt=$(("${#core[@]}" - 1))

for ((i = 0; i <= amt; i++)); do
    if ((i != amt)); then
        echo -n "${count[$i]} x ${core[$i]} + "
    else
        echo "${count[$i]} x ${core[$i]}"
        exit
    fi
done

# will print result like `4x Cortex-A55` or `4x Cortex-A53 + 2x Cortex-A72` - `lscpu` is built-in
