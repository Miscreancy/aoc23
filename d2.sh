#! /usr/bin/env bash

# Warning: the following solution is messy as heck

file=$1
operation=$2
pass_array=()
power_array=()
#touch newfile.txt
#: >newfile.txt

while read line; do
	game_id=$(echo $line | awk '{ print $2 }' | cut -f1 -d\:)
	amended_line=$(awk -F ':' '{ print $2 }' <<< $line )
	IFS=';' read -ra games <<< "${amended_line}"
	if [[ $operation -eq 2 ]]; then
		blue=0
		red=0
		green=0
	elif [[ $operation -eq 1 ]]; then
		pass="true"
	else
		echo "Invalid argument - must provide argument as to which puzzle you are trying to solve. Usage: ./d2sh filename (1|2)"
		exit 1
	fi
	for i in "${games[@]}"; do
		IFS=',' read -ra stages <<< "${i}"
		for stage in "${stages[@]}"; do	
			n=$(awk '{ print $1 }' <<< $stage)
			number=0
			let number+=$n
			colour=$(awk '{ print $2 }' <<< $stage)	
			case $colour in 
				blue)
					if [[ $operation -eq 2 ]]; then
						if [[ $number -gt $blue ]]; then
							blue=$number
						fi
					else
						if [[ $number -gt 14 ]]; then
							pass="false"
						fi
					fi
				;;
				green)
					if [[ $operation -eq 2 ]]; then
						if [[ $number -gt $green ]]; then
							green=$number
						fi
					else
						if [[ $number -gt 13 ]]; then
							pass="false"
						fi
					fi
				;;
				red)
					if [[ $operation -eq 2 ]]; then
						if [[ $number -gt $red ]]; then
							red=$number
						fi
					else
						if [[ $number -gt 12 ]]; then
							pass="false"
						fi
					fi
				;;
			esac
		done
	done
	if [[ $operation -eq 2 ]]; then
		power=$((${blue}*${red}*${green}))
		power_array+=("${power}")
	else
		if [[ $pass == "true" ]]; then
			pass_array+=("${game_id}")
		fi
	fi
done<$file

total=0
if [[ $operation -eq 2 ]]; then
	for integer in ${power_array[@]}; do
		let total+=$integer
	done
else
	for integer in ${pass_array[@]}; do
		let total+=$integer
	done
fi
echo $total
