import argparse
import ast

parser = argparse.ArgumentParser()
parser.add_argument(
   "-t", action="store_const", const="t", default="o", help="plik do zapisania, zamiast do odczytu", dest="tryb"
)
parser.add_argument(
   "-c", action="store_const", const="c", default="0", help="format csv", dest="csv"
)
parser.add_argument(
   "-j", action="store_const", const="a", default="0", help="format json", dest="json"
)

args = parser.parse_args()