# Assignment 1 - Data Mining
# Tytus Planck and Kyle Rossman
import csv
data = []
with open('income_tr.csv', 'rb') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in csvreader:
        dataRow = []
        for item in row:
            dataRow.append(item)
        data.append(dataRow)
print data[1][0]
