#!/bin/bash
case "$(dpkg --print-architecture)" in
amd64)
  mapfile -t core < <(lscpu | grep 'Model name' | sed -e 's/Model name\:                      //g' -e 's/with Radeon Graphics//g' -e 's/(R) Core(TM)//g')
  mapfile -t count < <(lscpu | grep 'CPU(s)' | awk '{print $2}') 
  ;;
arm64)
  mapfile -t core < <(lscpu | grep 'Model name' | awk '{print $3}')
  mapfile -t count < <(lscpu | grep 'per socket\|per cluster' | awk '{print $4}')
  ;;
esac

amt=$(("${#core[@]}" - 1))

for ((i = 0; i <= amt; i++)); do
    if ((i != amt)); then
        echo -n "${count[$i]} x ${core[$i]} + "
    else
        echo "${count[$i]} x ${core[$i]}"
        exit
    fi
done

# will print result like `4x Cortex-A55` or `4x Cortex-A53 + 2x Cortex-A72` or `24 x 13th Gen Intel i7-13700K` - `lscpu` is built-in