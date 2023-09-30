#!/usr/bin/env bash
#printing size of response body
echo "$(curl -sL -w "%{size_download}" -o /dev/null "$1")"
