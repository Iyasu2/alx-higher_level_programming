#!/usr/bin/env bash
#printing size of response body

if [ -z "$1" ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

echo "$(curl -sL -w "%{size_download}" -o /dev/null "$1")"
