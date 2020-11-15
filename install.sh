#!/bin/bash
echo "Don't forget to add env.py"

if test -f THE_SCRIPT_IS_INSTALLED; then
    echo "Already installed"
    exit 0
fi

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
PYTHON_MAIN_DIR=$DIR"/main.py"
echo $PYTHON_MAIN_DIR
(crontab -l 2>/dev/null; echo "@reboot nohup python3 "$PYTHON_MAIN_DIR" &") | crontab -
touch THE_SCRIPT_IS_INSTALLED