#!/bin/bash
if  pgrep -f "`dirname $0`"/pycalendar.py
then
    pkill -f "`dirname $0`"/pycalendar.py
else
    python "`dirname $0`"/pycalendar.py &
fi
