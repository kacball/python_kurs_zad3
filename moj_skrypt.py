# Przykład użycia: python3 moj_skrypt.py -m styczeń luty -d pn-wt pt -p r w
import argparse
import ast
# Miesiące w języku polskim
MONTHS = ["styczeń", "luty", "marzec", "kwiecień", "maj", "czerwiec", 
          "lipiec", "sierpień", "wrzesień", "październik", "listopad", "grudzień"]

# Dni tygodnia
DAYS = ["pn", "wt", "śr", "czw", "pt", "sb", "nd"]

parser = argparse.ArgumentParser()
parser.add_argument('-m', '--months', nargs='+', choices=MONTHS, required=True,
                    help="Wybierz miesiące, np. styczeń luty.")
parser.add_argument('-d', '--days', nargs='+', required=True,
                    help="Zakres dni tygodnia np. pn-wt pt.")
parser.add_argument('-p', '--times', nargs='+', choices=['r', 'w'], default=['r'],
                    help="Wybierz porę dnia: r - rano, w - wieczorem. Domyślnie rano.")
    
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