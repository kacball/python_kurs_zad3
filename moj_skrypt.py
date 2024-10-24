# Autorzy: Kacper Bal, Daniel Bernatowicz, Mateusz Mroczka, (??? dodaj się proszę :)
# Przykład użycia: python3 moj_skrypt.py -m styczen luty -d pn-wt pt -p r w
import argparse
import ast
import os
import random
import csv

def generate_random_data():
    model = random.choice(["A", "B", "C"])
    wynik = random.randint(0, 1000)
    czas = f"{random.randint(0, 1000)}s"
    return [model, wynik, czas]

def write_to_csv(file_path, data):
    header = ['Model', 'Wynik', 'Czas']

    with open(file_path, "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(header)
        writer.writerow(data)

time_sum = 0

def read_csv(file_path):
    global time_sum
    with open(file_path, "r", newline='', encoding='utf-8') as f:
        reader_csv = csv.DictReader(f, delimiter=';')
        for row in reader_csv:
            if row['Model'] == 'A':
                time_sum += int(row['Czas'][:-1])

# Miesiące w języku polskim
MONTHS = ["styczen", "luty", "marzec", "kwiecien", "maj", "czerwiec", 
          "lipiec", "sierpien", "wrzesien", "pazdziernik", "listopad", "grudzien"]

# Dni tygodnia
DAYS = ["pn", "wt", "sr", "czw", "pt", "sb", "nd"]

days_list = ['poniedzialek', 'wtorek', 'sroda', 'czwartek', 'piatek', 'sobota', 'niedziela']

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
months = args.months
days = args.days
what_time = args.times
read_or_write = args.tryb
if args.csv == "0":
    file_type = "json"
else:
    file_type = "csv"

times_index = 0
for i in range(len(months)):
    starting_day, ending_day = 0, 0
    if '-' in days[i]:
        period = days[i].split('-')
        starting_day = DAYS.index(period[0])
        ending_day = DAYS.index(period[1])
    else:
        starting_day = DAYS.index(days[i])
        ending_day = starting_day
    
    for j in range(starting_day, ending_day + 1):
        if times_index >= len(what_time):
            when = "rano"
        elif what_time[times_index] == "r":
            when = "rano"
        else:
            when = "wieczorem"
        
        # DEBUG LINE
        print(f"{months[i]} {days_list[j]} {when} {read_or_write} {file_type}")

        # Tworzenie ścieżki do pliku
        path = os.path.join(os.getcwd(), months[i], days_list[j], when)

        times_index +=1
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)

        if file_type == "csv":
            file_path = os.path.join(path, "Dane.csv")
            # Tworzenie pustych plików csv lub json jesli nie istnieja
            if not os.path.exists(file_path):
                with open(file_path, "w", encoding='utf-8') as f:
                    pass
            if read_or_write == "t":
                write_to_csv(file_path, generate_random_data())
            else:
                read_csv(file_path)
                
        else:
            file_path = os.path.join(path, "Dane.json")
            # Tworzenie pustych plików csv lub json jesli nie istnieja
            if not os.path.exists(file_path):
                with open(file_path, "w", encoding='utf-8') as f:
                    pass
            if read_or_write == "t":
                #TODO: zapis do pliku json
                pass
            else:
                #TODO odczyt z pliku json
                pass

if read_or_write != 't':
    print(f"Łączny czas w plikach, gdzie Model == 'A': {time_sum}")