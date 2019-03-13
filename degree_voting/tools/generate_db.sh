#!bin/bash

$(python3 manage.py makemigrations)
$(python3 manage.py migrate)
yes yes | $(python3 manage.py flush)
$(python3 manage.py db_manager)
echo "DB successfully created. New achievement unlocked!"