import csv

csv.register_dialect('dialect1',delimiter = ',', skipinitialspace = True)

with open('Ruby.csv', 'r' ) as File:
    reader = csv.reader(File, dialect='dialect1')
    for row in reader:
        print(row)