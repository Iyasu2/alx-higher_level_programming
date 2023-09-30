#!/bin/bash
#prints the methods allowed
curl -sI "$1" | grep -i '^allow:' | cut -d ' ' -f2-
