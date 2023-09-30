#!/usr/bin/env bash
#printing size of response body
curl -sL -w "%{size_download}" -o /dev/null "$1"; echo
