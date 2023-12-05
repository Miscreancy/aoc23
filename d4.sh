#! /usr/bin/env bash

filename=$1
operation=$2

case $operation in
	1)
		echo "Solving puzzle 1"
	;;
	2)
		echo "Solving puzzle 2"
	;;
	*)
		echo "Usage: d4.sh filename (1|2) - provide the inputfile and which puzzle you would like to solve"
		exit 1
	;;
esac

points=0
totalRepeats=0
declare -A indexRepeats
totalCards=$(cat $filename | wc -l)
for ((i=1; i<=$totalCards; ++i)); do
	indexRepeats+=(["$i"]=1)
done

while read line; do
	cardPoints=0
	matchPoints=0
	index=$( echo $line | awk -F ":" '{print $1 }' | awk '{ print $2 }')
	winners=$(echo $line | awk -F ":" '{ print $2 }' | awk -F "|" '{ print $1 }')
	holding=$(echo $line | awk -F ":" '{ print $2 }' | awk -F "|" '{ print $2 }')
	read -a numberArray <<< $holding
	read -a winnerArray <<< $winners
	repeats=${indexRepeats["$index"]}
	((totalRepeats+=repeats))
	((repeatIndex=index+1))
	for n in ${numberArray[@]}; do
		for w in ${winnerArray[@]}; do
			if [[ $n -eq $w ]]; then
				((++matchPoints))
				if [[ $cardPoints -eq 0 ]]; then
					((++cardPoints))
				else
					((cardPoints+=cardPoints))
				fi
			fi
		done
	done
	((points+=cardPoints))
	for ((i=1; i<=$matchPoints; ++i)); do
		currentRepeats=${indexRepeats["$repeatIndex"]}
		((currentRepeats+=repeats))
		indexRepeats["$repeatIndex"]=$currentRepeats
		((++repeatIndex))
	done
done<$filename

if [[ $operation -eq 1 ]]; then
	echo "Puzzle 1: $points"
else
	echo "Puzzle 2: $totalRepeats"
fi
