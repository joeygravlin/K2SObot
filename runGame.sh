#!/bin/bash

MY_BOT=MyBot.py
PYTHON=python

if hash python3 2>/dev/null; then
    PYTHON=python3
fi

for SOME_BOT in ./*Bot.py ; do
    ./halite -d "30 30" "$PYTHON $MY_BOT" "$PYTHON $SOME_BOT"
done
