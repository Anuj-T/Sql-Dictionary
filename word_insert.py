import tkinter as tk
from tkinter import messagebox
import mysql.connector


def insert_data(event = None):
	word = W.get()
	meaning = M.get()
	meaning_box.delete(first=0,last=255)
	word_box.delete(first=0,last=255)
	data = (word, meaning)
	conn = mysql.connector.connect(user='root', password='rogersachin', host='127.0.0.1', database='dictionary')
	cursor = conn.cursor()
	sql = """INSERT INTO vocabulary (word, meaning) VALUES (%s, %s)"""                     
	cursor.execute(sql, data)
	conn.commit()
	conn.close() 
	messagebox.showinfo("Success", "Word Inserted")
	print("Success")

root = tk.Tk()
root.title('Dictionary')
root.geometry("500x300")
root.bind('<Return>', insert_data)
W = tk.StringVar()
M = tk.StringVar()
word_box = tk.Entry(root, bd = 5, font = ('calibri', 20), textvariable = W)
word_box.place(x = 120, y = 50)

meaning_box = tk.Entry(root, bd = 5, font = ('calibri', 20), textvariable = M)
meaning_box.place(x = 120, y = 100)

insert_button = tk.Button(root, text ="Insert", padx = 10, pady = 10, command = insert_data,font = ('calibri', 15, 'bold'), foreground = 'red', background = 'black')

insert_button.place(x = 220, y = 150)


root.mainloop()

