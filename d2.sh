#!/usr/bin/env bash

# Warning: the following solution is messy as heck

file=$1
operation=$2
pass_array=()
power_array=()
#touch newfile.txt
#: >newfile.txt

case $operation in
	1)
		echo "Solving puzzle 1"
	;;
	2)
		echo "Solving puzzle 2"
	;;
	*)
		echo "Invalid arguments. Usage: ./d2sh filename (1|2)"
		exit 1
	;;
esac

declare -A limits=(["blue"]=14 ["green"]=13 ["red"]=12)

while read line; do
	game_id=$(echo $line | awk '{ print $2 }' | cut -f1 -d\:)
	amended_line=$(awk -F ':' '{ print $2 }' <<< $line )
	IFS=';' read -ra games <<< "${amended_line}"
	declare -A maximums=(["blue"]=0 ["green"]=0 ["red"]=0)
	pass="true"
	for i in "${games[@]}"; do
		IFS=',' read -ra stages <<< "${i}"
		for stage in "${stages[@]}"; do
			n=$(awk '{ print $1 }' <<< $stage)
			number=0
			let number+=$n
			colour=$(awk '{ print $2 }' <<< $stage)
			l=${limits["${colour}"]}
			limit=0
			let limit+=$l
			m=${maximums["${colour}"]}
			max=0
			let max+=$m
			if [[ $operation -eq 2 ]]; then
				if [[ $number -gt $max ]]; then
					maximums["${colour}"]=$number
				fi
			else
				if [[ $number -gt $limit ]]; then
					pass="false"
				fi
			fi
		done
	done
	if [[ $operation -eq 2 ]]; then
		blue=0
		red=0
		green=0
		b=${maximums["blue"]}
		let blue+=$b
		r=${maximums["red"]}
		let red+=$r
		g=${maximums["green"]}
		let green+=$g
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
