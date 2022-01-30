#!/bin/bash

sleep 1800

python3 /home/pi/Scripts/upload_log_on.py

sh /home/pi/Scripts/logs_RasPi.sh

python3 /home/pi/Scripts/upload_logs.py

gpio -g mode 4 out
gpio -g write 4 0
