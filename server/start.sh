#!/bin/bash
source /home/rmoreira97/projects/Mo/venv/bin/activate
cd /home/rmoreira97/projects/Mo/server
exec gunicorn -b 0.0.0.0:5000 "app:create_app"
echo "Python executable: $(which python)"
echo "PYTHONPATH: $PYTHONPATH"


