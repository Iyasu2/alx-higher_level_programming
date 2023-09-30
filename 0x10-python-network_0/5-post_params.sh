#!/bin/bash
#sending a variable
curl -sL "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
