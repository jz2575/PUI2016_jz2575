from __future__ import print_function
import pylab as pl
import json
import urllib2
import os
import sys
from sys import argv
import csv

VMD = 'VehicleMonitoringDelivery'
VA = 'VehicleActivity'
MVJ = 'MonitoredVehicleJourney'
VL = 'VehicleLocation'
OCs = 'OnwardCalls'
OC = 'OnwardCall'
PD = 'PresentableDistance'
SPN = 'StopPointName'

script, apikey, BUS_LINE, BUSCSV = argv
fout = open(BUSCSV, "w+")
fout.write("Latitude,Longitude,Stop Name,Stop Status\n")
if not len(sys.argv) == 4:
        print ("Invalid number of arguments.")
        print ("Run as: python show_bus_locations.py MTA-KEY BUS-LINE")

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?\
key=" + apikey + "&VehicleMonitoringDetailLevel=calls&LineRef=" + BUS_LINE
#print (url)

#url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key
#=15631ece-ce07-4e77-87b4-d82e87563051&VehicleMonitoringDetailLevel=calls&LineRef=B52"


response = urllib2.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)
#print (type(data))
#print (data)
va = data['Siri']['ServiceDelivery'][VMD][0][VA]
No_active_bus = len(va)
#print ('Bus Line: %s' %BUS_LINE)
#print ('Number of Active Buses : %d' %No_active_bus)
for i in range(len(va)):
    Long = va[i][MVJ][VL]['Longitude']
    Lat = va[i][MVJ][VL]['Latitude']
    if va[i][MVJ][OCs] == '':
        Pstop == 'N/A'
        StopName == 'N/A'
    else:
        PStop = va[i][MVJ][OCs][OC][0]['Extensions']['Distances'][PD]
        StopName = va[i][MVJ][OCs][OC][0][SPN]
    fout.write("%s,%s,%s,%s\n" %(Lat, Long, StopName, PStop))

fout.close()
with open(BUSCSV, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
    	print (row)