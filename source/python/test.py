import sys
import argparse 

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--users', help='add the names of the users you would like to generate the report on, example: iadams, "Isaac Adams"', nargs='+', required=True)
parser.add_argument('-t', '--time', help='the timeframe that you want to report on example: "1 week ago"', required=True)
args = parser.parse_args()
#print(args.users)

