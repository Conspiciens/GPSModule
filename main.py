import argparse
from os import read
import read_NMEA 

parser = argparse.ArgumentParser()

parser.add_argument("-SV", "--GPGSV", help="Displays GPS Satellites in View (GPGSV)", action="store_true")
parser.add_argument("-GA", "--GPGGA", help="Displays Global Positioning System Fix Data (GPGGA)", action="store_true")
parser.add_argument("-VTG", "--GPVTG", help="Displays Track Make Good and Ground Spped (GPVTG)", action="store_true")
parser.add_argument("-LL", "--GPGLL", help="Displays Geographic Position, Latitude / Longitude and Time (GPGLL)", action="store_true")
parser.add_argument("-RMC", "--GPRMC", help="Displays Recommended Minimum Specific GPS/Transit Data (GPRMC)", action="store_true")
parser.add_argument("-d", "--directory", help="Write directory where GPS module is printing strings (E.X = /dev/serial0)", action="store")

args = parser.parse_args()

GPS = read_NMEA.GPS_reader()

while str(input) != "q":
    exit = input()
    if args.GPGSV: 
        GPS.GPGSV_data()

    elif args.GPGGA:
        GPS.GPGGA_data()

    elif args.GPVTG:
        GPS.GPVTG_data()

    elif args.GPGLL: 
        GPS.GPGLL_data()

    elif args.GPRMC: 
        GPS.GPRMC_data()

    elif args.directory: 
        GPS.rewrite_directory(args.directory)
