# Bar-Sign
This is a sign I built for Drom, a bar on Queen st west.  It uses LED lights to show where the streetcar is

Basically I got a board wood burned to look like a 70s Eastern Block transit sign and put LED lights on it.  The wood is balsa, easy to burn and push the LED leds through, but somewhat fragile.

To adjust for your needs wire up a Raspberry PI to the GPIO slots, and then change the eastbound and westbound variables to whatever transit stops you need.

To add or edit wifi networks on a rapsberry pi from the command like use:
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
