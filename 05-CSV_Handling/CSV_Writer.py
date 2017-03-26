import csv

path = 'output.csv'

data = ['First Name, Last Name'.split(","),
        'Sachin, Tendulkar'.split(","),
        'Virat, Kohli'.split(","),
        'MS, Dhoni'.split(","),
        'John, Cena'.split(",")]

#data = ['SACHIN','C,D','E,F']

def csv_writer(path,data):

    with open(path,'w',newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')

        for line in data:
            writer.writerow(line)


csv_writer(path,data)
