#!/bin/bash
script_dir=$(cd "$(dirname "$0")"; pwd)
cd "$script_dir"

contents1=$(cat ./new_extensions.ps1)
contents2=$(cat ../extensions.ps1)

detected_encoding1=$(file -b --mime-encoding ./new_extensions.ps1)
detected_encoding2=$(file -b --mime-encoding ../extensions.ps1)

lines1=$(echo "$contents1" | iconv -f "$detected_encoding1" -t "$detected_encoding1" | tr -d '\r' | sed '/^#/ d; /^\s*$/d')
lines2=$(echo "$contents2" | iconv -f "$detected_encoding2" -t "$detected_encoding2" | tr -d '\r' | sed '/^#/ d; /^\s*$/d')

ps1_set=($lines1)
ps2_set=($lines2)

ps1_diff=$(echo ${ps1_set[@]} ${ps2_set[@]} | tr ' ' '\n' | uniq -u)
ps2_diff=$(echo ${ps2_set[@]} ${ps1_set[@]} | tr ' ' '\n' | uniq -u)


echo "ps1 have not: {$ps1_diff}"
printf "%0.s*" {1..100}; echo 
echo "ps2 have not: {$ps2_diff}"