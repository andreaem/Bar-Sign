#!/bin/bash

echo "SET wifi first!!! until the script is fixed"

echo "this shouldn't be run in sudo just fyi"

echo "choose a password"
passwd

sudo apt install git

git clone https://github.com/andreaem/Bar-Sign.git

sudo apt-get install python3-rpi.gpio

#the sudo isn't working quite right...
#echo "enter the SSID of the network"
#read ssid
#echo "enter the password of the network"
#read pw
#sudo echo 'country=CA' >> /etc/wpa_supplicant/wpa_supplicant.conf
#sudo echo 'network={ ssid="$ssid" psk="$pw" }' >> /etc/wpa_supplicant/wpa_supplicant.conf

sudo crontab ./crontab_config

#To lock machine to read only!
#wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/read-only-fs.sh 
#sudo bash read-only-fs.sh
