#! /usr/bin/env bash

# My original solution was too messy to publish. I've taken half the day to refactor and owe a lot to others on reddit and github for this solution
# If you look at the python implementation you can see a flavour of how I originally solved this; this way is neater

filename=$1
operation=$2

lines=($(tr '*.' G_ < "${1:-$filename}")) #replace * with G for gear - wildcard issues
sanitizedLines=(_${lines//?/_}_)

for i in "${lines[@]}"; do
	sanitizedLines+=(_${i}_)
done

sanitizedLines+=(${sanitizedLines[0]})
max=${#lines}

numbers=()

gears=()

declare -A stars
for ((y=1; y<=$max; ++y)); do # iterate over lines while lines -le the max, incrementing
    for ((x=1; x<=$max; ++x)); do # iterate over characters while character position -le the max, incrementing
        [[ ${sanitizedLines[y]:x:1} != [0-9] ]] && continue # skip if not equal to a d
        i=1
				num=

				while [[ ${sanitizedLines[y]:x+i:1} == [0-9] ]]; do
					((++i))
				done

				search=${sanitizedLines[y-1]:x-1:i+2}${sanitizedLines[y]:x-1:i+2}${sanitizedLines[y+1]:x-1:i+2}
				echo $search

        if ! [[ ${search} =~ ^[_0-9]*$ ]]; then
            numbers+=(${sanitizedLines[y]:x:i})
        fi

				# part 2

        if [[ $search == *G* ]]; then
            match=${search/G*}
            position=$((x-1+${#match}%(i+2))),$((y-1+${#match}/(i+2)))
            if [[ -n ${stars[$position]} ]]; then
                gears+=(${stars[$position]}*${numbers[-1]})
            else
                stars[$position]=${numbers[-1]}
            fi
        fi
        ((x+=i))
    done
done
if [[ $operation -eq 1 ]]; then
	printf -v sum "+%s" "${numbers[@]}"
	echo "$((sum))"
else
	printf -v sum "+%s" "${gears[@]}"
	echo "$((sum))"
fi
