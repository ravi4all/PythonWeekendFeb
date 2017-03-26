import csv

path = 'output.csv'

def csv_reader(path):

    # csv_file = open(path)
    with open(path) as csv_file:
        reader = csv.reader(csv_file, delimiter = ',')

        for row in reader:
            #print(row)
            print(row[0],row[1])


csv_reader(path)
