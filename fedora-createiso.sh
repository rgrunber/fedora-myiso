#! /bin/bash

if [ ! $# -eq 2 ]; then
	echo "Wrong number of arguments."
	exit 1
fi
if [ ! -e $1 ]; then
	echo "Kickstart file $1 is not valid."
	exit 1
fi

setarch $2 livecd-creator -c $1 -f Fedora-18-EclipseCon-Live-$2
