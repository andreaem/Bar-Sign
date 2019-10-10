#!/bin/bash

sudo apt install git

git clone https://github.com/andreaem/Bar-Sign.git

sudo apt-get install python3-rpi.gpio

#get userinfo for name and password
sudo echo 'country=CA' >> /etc/wpa_supplicant/wpa_supplicant.conf
sudo echo 'network={ ssid="testing" psk="testingPassword" }' >> /etc/wpa_supplicant/wpa_supplicant.conf

sudo crontab ./crontab_config

#To lock machine to read only!
#wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/read-only-fs.sh 
#sudo bash read-only-fs.sh
