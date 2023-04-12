#!/usr/bin/env bash

while IFS=':k '  read -r key val _; do
    case $key in
        (MemTotal)
            mem_used=$((mem_used + val))
            mem_full=$val
        ;;

        (Shmem)
            mem_used=$((mem_used + val))
        ;;

        (MemFree | Buffers | Cached | SReclaimable)
            mem_used=$((mem_used - val))
        ;;

        (MemAvailable)
            mem_avail=$val
        ;;
    esac
done < /proc/meminfo

case $mem_avail in
    (*[0-9]*)
        mem_used=$(((mem_full - mem_avail) / 1024))
    ;;

    *)
        mem_used=$((mem_used / 1024))
    ;;
esac

echo $((mem_full / 1024))