# csv.reader e csv.DictReader
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path

CSV_PATH = Path(__file__).parent / 'aula293.csv'
print(CSV_PATH)

with open(CSV_PATH, 'r') as file:
    reader = csv.DictReader(file)

    for line in reader:
        print(line)

# with open(CSV_PATH, 'r') as file:
#     reader = csv.reader(file)

#     # print(next(file))

#     for line in reader:
#         print(line)
