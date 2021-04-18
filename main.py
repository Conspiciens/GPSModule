import argparse
import read_NMEA 

read_string = read_NMEA.Serial_reader()

parser = argparse.ArgumentParser()

parser.add_argument("-SV", "--GPGSV", help="Displays GPS Satellites in View (GPGSV)", action="store_true")
parser.add_argument("-GA", "--GPGGA", help="Displays Global Positioning System Fix Data (GPGGA)", action="store_true")
parser.add_argument("-VTG", "--GPVTG", help="Displays Track Make Good and Ground Spped (GPVTG)", action="store_true")
parser.add_argument("-LL", "--GPGLL", help="Displays Geographic Position, Latitude / Longitude and Time (GPGLL)", action="store_true")
parser.add_argument("-RMC", "--GPRMC", help="Displays Recommended Minimum Specific GPS/Transit Data (GPRMC)", action="store_true")
parser.add_argument("-d", "--directory", help="Write directory where GPS module is printing strings (E.X = /dev/serial0)", action="store")

args = parser.parse_args()

if args.GPGSV:
    while True:  
        read_string.GPGSV_data()

elif args.GPGGA:
    read_string.GPGGA_data()

elif args.GPVTG:
    read_string.GPVTG_data()

elif args.GPGLL: 
    read_string.GPGLL_data()

elif args.GPRMC: 
    read_string.GPRMC_data()

elif args.directory: 
    read_string.rewrite_directory(args.directory)