#!/bin/bash
# Activate your virtual environment (replace with your virtual environment activation command)
source /opt/render/project/src/.venv/bin/activate

# Navigate to the server directory (replace with the correct path on Render)
cd /opt/render/project/src/server

exec gunicorn -b 0.0.0.0:5000 "app:flask_app"



