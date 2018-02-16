#!/bin/sh

heroku run python manage.py dumpdata actions habits --natural-foreign -- > tmpdump.json
./manage.py loaddata tmpdump.json
if [ $? -eq 0 ]; then
    echo OK
    rm tmpdump.json
else
    echo FAIL. Check tmpdump.json and try importing manually, or try again later.
fi
