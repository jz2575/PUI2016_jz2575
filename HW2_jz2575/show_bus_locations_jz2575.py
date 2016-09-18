from __future__ import print_function
import pylab as pl
import json
import urllib2
import os
import sys
from sys import argv

script, apikey, BUS_LINE = argv
if len(sys.argv) != 3:
        print ("Invalid number of arguments.")
        print ("Run as: python show_bus_locations.py MTA-KEY BUS-LINE")

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?\
key=" + apikey + "&VehicleMonitoringDetailLevel=calls&LineRef=" + BUS_LINE
#print (url)

#url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=15631ece-ce07-4e77-87b4-d82e87563051&VehicleMonitoringDetailLevel=calls&LineRef=B52"


response = urllib2.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)
#print (type(data))
#print (data)
#Ser_Del = ServiceDelivery
Ser_Del = data['Siri']['ServiceDelivery'] 
#Veh_Act = VehicleActivity
Veh_Act = Ser_Del['VehicleMonitoringDelivery'][0]['VehicleActivity']
No_active_bus = len(Veh_Act)
print ('Bus Line : %s' %BUS_LINE)
print ('Number of Active Buses : %d' %No_active_bus)
for i in range(len(Veh_Act)):
    Long = Veh_Act[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    Lat = Veh_Act[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    print ('Bus %d is at latitude %r and longitude %r' %(i, Lat, Long))
