#!/bin/bash

X="$1"
if [[ -z "$X" ]]; then
	echo Enter soundcloud url ": " 
	read X
fi	
mplayer $(python soundcloudstreamer.py -q "$X")