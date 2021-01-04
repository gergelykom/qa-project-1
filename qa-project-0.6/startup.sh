#!/bin/bash
export DATABASE_URI='mysql+pymysql://root:groot@35.234.132.64/flask_db'
cd /opt/qa-project
sudo python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 app.py