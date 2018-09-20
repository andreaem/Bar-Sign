''' Streetcar LED light up sign for Drom Bar.  By Michael Andreae 2018 '''
''' enter @reboot python3 /home/pi/Desktop/pythonSign.py & in sudo crontab -e, eg the cron tab, and it will start on startup'''
#Get the URL and then display in LED's
import time
import urllib.request
from xml.dom import minidom
import RPi.GPIO as GPIO

#https://thepihut.com/blogs/raspberry-pi-tutorials/27968772-turning-on-an-led-with-your-raspberry-pis-gpio-pins

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#[raspberry pi pin, stop code, stop name]

eastbound = [
[2,'15139', "Sudbury"],
[2,'5899', "Abell"],
[3,'8263', "Dovercourt"],
[4,'9093', "Ossington"],
[17,'2140', "Shaw"],
[27,'5250', "Strachan"],
[22,'3896', "Niagara"],
[5,'3399', "Tecumseth"],
[6,'4514', "Bathurst"],
[25,'8269', "Augusta"],
]

westbound = [
[24,'1958', "Victoria St"],
[24,'2332', "Yonge"],
[23,'2240', "Bay"],
[18,'4413', "York"],
[15,'2086', "University"],
[14,'15131', "St Patrick"],
[26,'6851', "John"],
[19,'704', "Peter"],
[13,'1653', "Spadina"],
[21,'3624', "Augusta"],
]

''' Creates the URL to get the stop info from '''
#to get a list of all stops, note there's east and westbound
#http://webservices.nextbus.com/service/publicXMLFeed?command=routeConfig&a=ttc&r=501
AddStopURL = "http://webservices.nextbus.com/service/publicXMLFeed?command=predictionsForMultiStops&a=ttc"
for stop in range(len(westbound)):
    AddStopURL = AddStopURL + "&stops=501|" + str(westbound[stop][1])
for stop in range(len(eastbound)):
    AddStopURL = AddStopURL + "&stops=501|" + str(eastbound[stop][1])

''' Initialize the LED pins as general IO pins'''
for bulb in eastbound:
    GPIO.setup(bulb[0],GPIO.OUT)
for bulb in westbound:
    GPIO.setup(bulb[0],GPIO.OUT)

''' Sets all the LEDs to off '''
def resetStops():
    for bulb in eastbound:
        GPIO.output(bulb[0],GPIO.LOW)
    for bulb in westbound:
        GPIO.output(bulb[0],GPIO.LOW)
resetStops()

''' Run a diagnostic, ensures all lights are working and that the WiFi has time to connect on bootup '''
def runDiagnostic(finalLoop):
  i = 0
  while (i != finalLoop) :
    i += 1
    for bulb in eastbound:
        print (bulb)
        GPIO.output(bulb[0],GPIO.HIGH)
        time.sleep(1)
        GPIO.output(bulb[0],GPIO.LOW)

    for bulb in westbound:
        print (bulb)
        GPIO.output(bulb[0],GPIO.HIGH)
        time.sleep(1)
        GPIO.output(bulb[0],GPIO.LOW)
    resetStops()
    time.sleep(2)


'''returns a dictionary with the vehicle number of the next car to that stop'''
def getNextCar() :
    minbase=99
    contents = urllib.request.urlopen(AddStopURL).read()
    contents = contents.decode("utf-8")
    xmldoc = minidom.parseString(contents)
    allStopPrediction = xmldoc.getElementsByTagName('predictions')
    returnVal = {}
    for i in allStopPrediction:
      itemlist = i.getElementsByTagName('prediction')
      for s in itemlist: #.getElementsByTagName('direction'):
        if ((s.attributes['minutes'].value).isdigit()):
            if (minbase > int(s.attributes['minutes'].value)):
                returnVal[i.attributes['stopTag'].value] = s.attributes['vehicle'].value
                minbase = int(s.attributes['minutes'].value)
      minbase=99
    return returnVal

''' Initialize '''
runDiagnostic(1)

'''Main loop'''
while(True):
    NextTrainDict = getNextCar()
    resetStops()

    for stop in range(len(westbound)-1):
        if NextTrainDict[westbound[stop][1]] != NextTrainDict[westbound[stop+1][1]]:
            GPIO.output(westbound[stop+1][0],GPIO.HIGH)

    for stop in range(len(eastbound)-1):
        if NextTrainDict[eastbound[stop][1]] != NextTrainDict[eastbound[stop+1][1]]:
            GPIO.output(eastbound[stop+1][0],GPIO.HIGH)

    time.sleep(10)
