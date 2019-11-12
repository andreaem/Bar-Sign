# Bar-Sign
This is a sign I built for Drom, a bar on Queen st west.  It uses LED lights to show where the streetcar is.  The sign is made out of a balsa wood burned sheet framed by stretcher bars for a canvas.  The balsa wood was easy to burn and push the LED leds through, but somewhat fragile.

To adjust for your needs wire up a Raspberry PI to the GPIO slots, and then change the eastbound and westbound variables to whatever transit stops you need.

Info about the read only mode, the sign was crashing doing memory writes
https://learn.adafruit.com/read-only-raspberry-pi?view=all.

INSTALL

Download raspbian lite and install to usb
https://www.raspberrypi.org/downloads/raspbian/

sudo apt install git

git clone https://github.com/andreaem/Bar-Sign.git

Run the script to auto initilaize.

# Notes:

WIFICONFIG:

NOTE capitalization matters for the name and password!  Also you can only put in one network id using this syntax.

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
