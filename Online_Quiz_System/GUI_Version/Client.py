import socket
import tkinter as tk
from tkinter import messagebox

def send_test_choice():
    test_choice = test_var.get()
    client_socket.sendall(test_choice.encode())

    # Receive response from the main server
    response = client_socket.recv(1024)
    response_label.config(text="Response: " + response.decode())

    msg = "Okay"
    client_socket.sendall(msg.encode())

def send_answer():
    answer = answer_entry.get()
    client_socket.sendall(answer.encode())
    response = client_socket.recv(1024)
    response_label.config(text=response.decode())

def close_connection():
    Marks = client_socket.recv(1024)
    response_label.config(text="Marks: " + Marks.decode())
    # client_socket.close()
    # root.destroy()

# Create the socket object and connect to the main server
MAIN_SERVER_HOST = '127.0.0.1'
MAIN_SERVER_PORT = 12345
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((MAIN_SERVER_HOST, MAIN_SERVER_PORT))

# Create the GUI
root = tk.Tk()
root.title("Test Selection")

test_var = tk.StringVar()

test_label = tk.Label(root, text="Choose the Test:")
test_label.pack()

math_radio = tk.Radiobutton(root, text="Mathematics", variable=test_var, value="1")
math_radio.pack()

prog_radio = tk.Radiobutton(root, text="Programming", variable=test_var, value="2")
prog_radio.pack()

eng_radio = tk.Radiobutton(root, text="English", variable=test_var, value="3")
eng_radio.pack()

send_button = tk.Button(root, text="Send Test Choice", command=send_test_choice)
send_button.pack()


response_label = tk.Label(root, text="")
response_label.pack()

question_label = tk.Label(root, text="Enter your answer:")
question_label.pack()

answer_entry = tk.Entry(root)
answer_entry.pack()

send_answer_button = tk.Button(root, text="Send Answer", command=send_answer)
send_answer_button.pack()

close_button = tk.Button(root, text="Close Connection", command=close_connection)
close_button.pack()


root.mainloop()
