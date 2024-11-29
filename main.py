import tkinter
from tkinter import messagebox
import csv

def read_data():
    table = []
    with open('soccer_stats.csv', mode ='r') as file:
        file.readline()
        csvfile = csv.reader(file)
        for line in csvfile:
            if not line == []:
                table.append(line)
    return table
def display_data():
    statistics = read_data()
    display_text = ""
    for i in statistics:
        display_text += "First Name: " + i[0] + ", Last Name: " + i[1] + ", G/A: " + str(i[2]) + ", Games Won: " + str(i[3]) + "\n"
    window.players_label.config(text=display_text)

def add_to_csv(stats):
    with open("soccer_stats.csv", mode='a', newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow(stats)
def write_to_csv(stats):
    with open("soccer_stats.csv", mode='w', newline='') as file:
        file.writelines("first_name,last_name,goals_assists,games_won\n")
        writer = csv.writer(file)
        writer.writerows(stats)
def delete_from_csv(firstname, lastname):
    statistics_data = read_data()
    new_data = []
    for i in statistics_data:
        if not (i[0] == firstname and i[1] == lastname):
            new_data.append(i)
    write_to_csv(new_data)

def create_data():
    firstname_value = window.firstname_entry.get().strip()
    lastname_value = window.lastname_entry.get().strip()
    ga_value = window.GA_entry.get().strip()
    games_value = window.games_entry.get().strip()
    if not ga_value.isdigit():
        messagebox.showerror("Invalid G/A statistics", "G/A statistics must be a number.")
        return
    if not games_value.isdigit():
        messagebox.showerror("Invalid Games Won statistics", "Games Won statistics must be a number.")
        return
    if not firstname_value or not lastname_value or not ga_value or not games_value:
        messagebox.showerror("Invalid Input", "First Name, Last Name, G/A and Games Won statistics input must be valid")
        return
    add_to_csv([firstname_value, lastname_value, ga_value, games_value])
    messagebox.showinfo("Success", "New Ballon d'Or player statistic added successfully.")
    delete_entries()

def update_data():
    firstname_value = window.firstname_entry.get().strip()
    lastname_value = window.lastname_entry.get().strip()
    ga_value = window.GA_entry.get().strip()
    games_value = window.games_entry.get().strip()
    if not ga_value.isdigit():
        messagebox.showerror("Invalid G/A statistics", "G/A statistics must be a number.")
        return
    if not games_value.isdigit():
        messagebox.showerror("Invalid Games Won statistics", "Games Won statistics must be a number.")
        return
    if not firstname_value or not lastname_value or not ga_value or not games_value:
        messagebox.showerror("Invalid Input", "First Name, Last Name, G/A and Games Won statistics input must be valid")
        return
    statistics_data = read_data()
    for i in range(len(statistics_data)):
        if statistics_data[i][0] == firstname_value and statistics_data[i][1] == lastname_value:
            statistics_data[i] = [firstname_value, lastname_value, ga_value, games_value]
            write_to_csv(statistics_data)
            messagebox.showinfo("Success", "Ballon d'Or statistics updated successfully.")
            delete_entries()
            return
    messagebox.showerror("Error", "Player not found.")


def delete_data():
    firstname_value = window.firstname_entry.get().strip()
    lastname_value = window.lastname_entry.get().strip()
    ga_value = window.GA_entry.get().strip()
    games_value = window.games_entry.get().strip()
    if not ga_value.isdigit():
        messagebox.showerror("Invalid G/A statistics", "G/A statistics must be a number.")
        return
    if not games_value.isdigit():
        messagebox.showerror("Invalid Games Won statistics", "Games Won statistics must be a number.")
        return
    if not firstname_value or not lastname_value or not ga_value or not games_value:
        messagebox.showerror("Invalid Input", "First Name, Last Name, G/A and Games Won statistics input must be valid")
        return
    statistics_data = read_data()
    for i in range(len(statistics_data)):
        if statistics_data[i][0] == firstname_value and statistics_data[i][1] == lastname_value:
            delete_from_csv(firstname_value, lastname_value)
            messagebox.showinfo("Success", "Player removed from Ballon d'Or rankings successfully.")
            delete_entries()
            return
    messagebox.showerror("Error", "Player not found.")

def delete_entries():
    window.firstname_entry.delete(0, tkinter.END)
    window.lastname_entry.delete(0, tkinter.END)
    window.GA_entry.delete(0, tkinter.END)
    window.games_entry.delete(0, tkinter.END)


window = tkinter.Tk()
window.title("Ballon d'Or Rankings")
window.minsize(600, 400)
window.input_frame = tkinter.Frame()
window.buttons_frame = tkinter.Frame()
window.records_frame = tkinter.Frame()
window.firstname_label = tkinter.Label(window.input_frame, text="First Name:")
window.lastname_label = tkinter.Label(window.input_frame, text="Last Name:")
window.GA_label = tkinter.Label(window.input_frame, text="Goals + Assists: ")
window.games_label = tkinter.Label(window.input_frame, text="Games Won: ")
window.players_label = tkinter.Label(window.records_frame, text="The Top Ballon d'Or Players will be displayed here")

window.firstname_entry = tkinter.Entry(window.input_frame)
window.lastname_entry = tkinter.Entry(window.input_frame)
window.GA_entry = tkinter.Entry(window.input_frame)
window.games_entry = tkinter.Entry(window.input_frame)


window.create_button = tkinter.Button(window.buttons_frame, text="Create", command=create_data)

window.read_button = tkinter.Button(window.buttons_frame, text="Read", command=display_data)

window.update_button = tkinter.Button(window.buttons_frame, text="Update", command=update_data)

window.delete_button = tkinter.Button(window.buttons_frame, text="Delete", command=delete_data)

window.input_frame.pack(pady=10)
window.buttons_frame.pack(pady=10)
window.records_frame.pack(pady=10)


window.firstname_label.grid(row=0, column=0, padx=10, pady=5)
window.firstname_entry.grid(row=0, column=1, padx=10, pady=5)

window.lastname_label.grid(row=1, column=0, padx=10, pady=5)
window.lastname_entry.grid(row=1, column=1, padx=10, pady=5)

window.GA_label.grid(row=2, column=0, padx=10, pady=5)
window.GA_entry.grid(row=2, column=1, padx=10, pady=5)

window.games_label.grid(row=3, column=0, padx=10, pady=5)
window.games_entry.grid(row=3, column=1, padx=10, pady=5)

window.players_label.grid(row=0, column=0, padx=10, pady=10)


window.create_button.grid(row=0, column=0, padx=10, pady=10)

window.read_button.grid(row=0, column=1, padx=10, pady=10)

window.update_button.grid(row=0, column=2, padx=10, pady=10)

window.delete_button.grid(row=0, column=3, padx=10, pady=10)



window.mainloop()