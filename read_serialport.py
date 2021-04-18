import serial
import socket

ser = serial.Serial('/dev/serial0')
latitude = ''
longitude = ''

def readgps(latitude,longitude):
        """Read the GPG LINE using the NMEA standard"""
        while True:
                line = ser.readline()
                if "GPGGA" in line:
                        gpdd = line.split(',')
                        GPGGA_data(gpdd)

                if "GPVTG" in line:
                        gpvtgd = line.split(',')
                        GPVTG_data(gpvtgd)

                if "GPRMC" in line:
                        gprmcd = line.split(',')
                        GPRMC_data(gprmcd)

        print ("Finished")

def GPGGA_data(gpdd):
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
        print ("---------------------------------")

def GPVTG_data(gpvtgd):
        print ("Track Made Good and Ground Speed")
        print ("Track Made Good: " + gpvtgd[1] + gpvtgd[2])
        print ("None: " + gpvtgd[3])
        print ("None: " + gpvtgd[4])
        print ("Speed over ground in Knots: " + gpvtgd[5]+ gpvtgd[6])
        print ("Speed over ground in kilometers/hour: " + gpvtgd[7] + gpvtgd[8])
        print ("Checksum: " + gpvtgd[9])
        print ("----------------------------------")

def GPRMC_data(gpmrcd):
        print ("Vadility: " + gpmrcd[2])
