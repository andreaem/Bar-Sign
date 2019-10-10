# Bar-Sign
This is a sign I built for Drom, a bar on Queen st west.  It uses LED lights to show where the streetcar is

Basically I got a board wood burned to look like a 70s Eastern Block transit sign and put LED lights on it.  The wood is balsa, easy to burn and push the LED leds through, but somewhat fragile.

To adjust for your needs wire up a Raspberry PI to the GPIO slots, and then change the eastbound and westbound variables to whatever transit stops you need.

INSTALL

Download raspbian lite and install to usb
https://www.raspberrypi.org/downloads/raspbian/

sudo apt install git

git clone https://github.com/andreaem/Bar-Sign.git

sudo apt-get install python3-rpi.gpio

WIFICONFIG:

sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
SET ->

country=CA
network={
    ssid="testing"
    psk="testingPassword"
}

AUTOSTART

sudo crontab -e

SET->
@reboot python3 /home/pi/Bar-Sign/pythonSign.py &  

COMMIT TO READ ONLY

wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/read-only-fs.sh
sudo bash read-only-fs.sh
