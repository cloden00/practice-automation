#!/usr/bin/env bash

source venv/bin/activate

printf "\t\tAUTOMATION SUITE START\n\n" > script.log

printf "\tPlaywright UI Tests:\n" >> script.log
python3 day03_ui_loop.py >> script.log 2>&1

printf "\n\tBackend API Tests:\n" >> script.log 
python3 day05_api_test.py >> script.log 2>&1