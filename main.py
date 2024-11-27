import tkinter
import csv

def read_data():
    table = []
    with open('soccer_stats.csv', mode ='r') as file:
        csvFile = csv.reader(file)
        for line in csvFile:
            print(line)
            table.append(line)
    print(table)
read_data()