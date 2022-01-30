#!/bin/bash

echo "************** XBG HRCam PUIGCERCOS logs **************" >> /home/pi/logs/log_RaspPi.log
echo "$(date) @ $(hostname)" >> /home/pi/logs/log_RaspPi.log
echo >> /home/pi/logs/log_RaspPi.log
echo "Temp.CPU => $((cpu/1000))'Cº" >> /home/pi/logs/log_RaspPi.log
echo "Temp GPU => $(/opt/vc/bin/vcgencmd measure_temp)" >> /home/pi/logs/log_RaspPi.log
echo "CPU $(vcgencmd measure_volts core)'Hz" >> /home/pi/logs/log_RaspPi.log
echo "CPU $(vcgencmd measure_clock arm)'Hz" >> /home/pi/logs/log_RaspPi.log
echo >> /home/pi/logs/log_RaspPi.log >> /home/pi/logs/log_RaspPi.log
echo "Us memoria RAM" >> /home/pi/logs/log_RaspPi.log
echo "$(free --mega -t)" >> /home/pi/logs/log_RaspPi.log
echo >> /home/pi/logs/log_RaspPi.log >> /home/pi/logs/log_RaspPi.log
echo "Memoria total disponible" >> /home/pi/logs/log_RaspPi.log
echo "$(df -P --total -Bg -h)" >> /home/pi/logs/log_RaspPi.log
echo >> /home/pi/logs/log_RaspPi.log
sudo iwconfig wlan0 >> /home/pi/logs/log_RaspPi.log
echo >> /home/pi/logs/log_RaspPi.log

cp /home/pi/wittypi/schedule.log /home/pi/wittypi/wittyPi.log /home/pi/logs

