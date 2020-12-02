#!/bin/bash
if test -f THE_SCRIPT_IS_INSTALLED; then
    echo "Already installed"
    exit 0
fi

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
parentdir="$(dirname "$DIR")"
mkdir $parentdir"/localWebsites"

(crontab -l 2>/dev/null; echo "@reboot cd "$DIR" && nohup python3 main.py&") | crontab -
touch THE_SCRIPT_IS_INSTALLED