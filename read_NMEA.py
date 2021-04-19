import dotenv
import serial
import os
from dotenv import load_dotenv

def start_serial(): 
    return serial.Serial(get_directory())

def get_directory():
    dotenv_file = dotenv.find_dotenv('directory_value.env')
    dotenv.load_dotenv(dotenv_file)
    return os.environ["DIRECTORY"]
    
def rewrite_directory(dir):
    dotenv_file = dotenv.find_dotenv('directory_value.env')
    dotenv.load_dotenv(dotenv_file)
    os.environ["DIRECTORY"] = dir
    dotenv.set_key(dotenv_file, "DIRECTORY", os.environ["DIRECTORY"])

def read_nvmea():
    line = start_serial().readline().decode()
    list_info = line.split(',')
    return list_info

def GPGGA_data():  
    gpdd = read_nvmea()

    print ("Global Positioning Data")
    print ("Time: " + gpdd[1])
    print ("Latitude: " + gpdd[2]+ gpdd[3])
    print ("Longtitude: " + gpdd[4] + gpdd[5])
    print ("Fix Quality: " + gpdd[6])
    print ("Num Satellites: " + gpdd[7])
    print ("HDOP: " + gpdd[8])
    print ("Altitude: " + gpdd[9] + gpdd[10])
    print ("Height Above Ellipsiodal Height: " + gpdd[11] + gpdd[12])
    print ("Last DGPS update: " + gpdd[13])
    # print ("DGPS Reference station ID: " + gpdd[14])
    print ("Checksum: " + gpdd[14])
    print ("----------------------------------")
    
def GPVTG_data():
    gpvtgd = read_nvmea() 

    print ("Track Made Good and Ground Speed")
    print ("Track Made Good: " + gpvtgd[1] + gpvtgd[2])
    print ("None: " + gpvtgd[3])
    print ("None: " + gpvtgd[4])
    print ("Speed over ground in Knots: " + gpvtgd[5]+ gpvtgd[6])
    print ("Speed over ground in kilometers/hour: " + gpvtgd[7] + gpvtgd[8])
    print ("Checksum: " + gpvtgd[9])
    print ("----------------------------------")
    
def GPRMC_data():
    gpmrcd = read_nvmea()

    print ("Recommended minimum specific GPS/Transit data")
    print ("Vadility: " + gpmrcd[2])
    print ("Speed over ground in knots: " + gpmrcd[7])
    print ("Track in Degrees: " + gpmrcd[8])
    print ("UT Date: " + gpmrcd[9])
    print ("Magnetic variation degrees: " + gpmrcd[10] + gpmrcd[11])
    print ("Checksum: " + gpmrcd[12])
    print ("----------------------------------")

def GPGSV_data(gpgsvd): 
    # gpgsvd = read_nvmea()

    print ("GPS Satellites in View")
    print ("Total Number of Messages in Cycle: " + gpgsvd[1])
    print ("Message Number: " + gpgsvd[2])
    print ("Total number of SV in view: " + gpgsvd[3])
    print ("SV PRN Number: " + gpgsvd[4])
    print ("Elevation in degrees: " + gpgsvd[5])
    print ("Azimuth degrees from true North: " + gpgsvd[6])
    # 8-11 = Information about second SV, same as field 4-7
    # 12-15= Information about third SV, same as field 4-7
    # 16-19= Information about fourth SV, same as field 4-7
    print ("----------------------------------")

def GPGLL_data():
    gpglld = read_nvmea()

    print ("Geographic Position, Latitude / Longitude and time")
    print ("Current Latitude: " + gpglld[1] + ' ' + gpglld[2])
    print ("Current Longitude: " + gpglld[3] + ' ' + gpglld[4])
    print ("Checksum: " + gpglld[5])
    print ("----------------------------------")


GPGGA_data()
