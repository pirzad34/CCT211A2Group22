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
'''
def create_data():
def update_data():
def delete_data():
Potential features + more
'''

window = tkinter.Tk()
window.title("Soccer Stats")
window.minsize(800, 400)