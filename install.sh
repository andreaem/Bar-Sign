#!/bin/bash

echo "SET wifi first!!! until the script is fixed"

echo "this shouldn't be run in sudo just fyi"

echo "choose a password, enter your old one first"
passwd

sudo apt install git

git clone https://github.com/andreaem/Bar-Sign.git

sudo apt-get install python3-rpi.gpio

sudo sed -i '$ d' /etc/rc.local
sudo bash -c 'echo "python3 /home/py/Bar-Sign/pythonSign.py" >> /etc/rc.local'
sudo bash -c 'sudo echo "exit 0" >> /etc/rc.local'

#the sudo isn't working quite right...
echo "enter the SSID of the network"
read ssid
echo "enter the password of the network"
read pw
echo 'country=CA' | sudo tee -a /etc/wpa_supplicant/wpa_supplicant.conf
echo 'network={ ssid="$ssid" psk="$pw" }' | sudo tee -a /etc/wpa_supplicant/wpa_supplicant.conf

#doesn't work on locked down system
#sudo crontab ./crontab_config

#To lock machine to read only!
#wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/read-only-fs.sh 
#sudo bash read-only-fs.sh
