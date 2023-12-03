#! /usr/bin/env bash

og_file=$1
operation=$2

case $operation in
	1)
		echo "Solving puzzle 1"	
	;;
	2)
		echo "Solving puzzle 2"
	;;
	*)
		echo "Usage: d1.sh filename (1|2) - provide the inputfile and which puzzle you would like to solve"
		exit 1
	;;
esac

touch numberfile.txt
: > numberfile.txt
cp $og_file new_file.txt
file="new_file.txt"

if [[ $operation -eq 2 ]]; then
	sed -i 's/one/one1one/g' $file
	sed -i 's/two/two2two/g' $file
	sed -i 's/three/three3three/g' $file
	sed -i 's/four/four4four/g' $file
	sed -i 's/five/five5five/g' $file
	sed -i 's/six/six6six/g' $file
	sed -i 's/seven/seven7seven/g' $file
	sed -i 's/eight/eight8eight/g' $file
	sed -i 's/nine/nine9nine/g' $file
	sed -i 's/zero/zero0zero/g' $file
fi

while read line; do
	numberArray=()
	while [[ "$line" =~ [0-9] ]]; do
		numberArray+=(${BASH_REMATCH[0]})
		line="${line#*"${BASH_REMATCH[0]}"}"
	done
	number="${numberArray[0]}${numberArray[-1]}"
	echo $number>>numberfile.txt
done<$file

awk '{sum+=$1} END {print sum}' numberfile.txt

rm numberfile.txt
rm new_file.txt
