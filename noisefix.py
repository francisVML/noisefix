# Modify JSON Cal file
from ctypes import *
import json
import requests
import os.path

url = 'http://localhost/api/sensors/0/'
#replace path with current Documents folder path in the directory
path = 'C:/Users/fnatividad/Documents/'

level = [ 1,0,0,0,0,0,0,0,0,0,0 ] 

#  Serial number
serial = requests.get(url+'name').json()
print (serial)

data = requests.get(url+'calibration')
calfile = data.json()
with open(path+serial+"og.json", "w") as data_file:
    json.dump(calfile, data_file)
print ("Original Calfile Downloaded")

# while loop to multiply existing calfile with the multipliers
c = 0
zero = calfile ['filters'] [1] ['samples'] [0]
#print (hyst)
mod = [None] * len (zero)
j = 0
for cell in zero:
    mod [j] = 80
    j += 1
calfile ['filters'] [1] ['samples'] [c] = mod


# Load modified cal file into sensor
requests.put(url+"calibration", json=calfile) 

# save a copy of the modified calibration file
with open(path+serial+"ns.json", "w") as data_file:
    json.dump(calfile, data_file)
    
print('Done')

input ("Press Enter to Exit") 