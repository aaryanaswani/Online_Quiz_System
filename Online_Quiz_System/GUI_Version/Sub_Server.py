import socket


# Function for Quizes:
def Mathematics():
    score = 0    
    Instructions="Instructions\n-You will be given 3 Questions during your Quiz Answer them one by one.\n-Each Question holds 10 marks\n"
    client_socket.sendall(Instructions.encode())

    response = client_socket.recv(1024)
    
    if response.decode() == "Okay":
        questions = [
         ("Question 1: What is the result of 5 + 7?", "12"),
         ("Question 2: What is the square root of 64?", "8"),
         ("Question 3: What is the value of π (pi) rounded to two decimal places?", "3.14")
        ]

        for question, answer_key in questions:
            client_socket.sendall(question.encode())
            answer = client_socket.recv(1024)
            if answer.decode() == str(answer_key):
                print("Correct!\n")
                score = score + 10
            else:
                print("Not Correct...\n")

        out = "EXIT"
        out = str(out)
        client_socket.sendall(out.encode())
    
    response = client_socket.recv(1024)
    if response.decode() == "Done":
        asd = str(score)
        return asd

def Programming():
    score = 0    
    Instructions="Instructions\n-You will be given 3 Questions during your Quiz Answer them one by one.\n-Each Question holds 10 marks\n"
    client_socket.sendall(Instructions.encode())

    response = client_socket.recv(1024)
    
    if response.decode() == "Okay":
        questions = [
        ("What is the name of the sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order?", "bubble"),
        ("In object-oriented programming, what is the term for creating a new instance of a class?", "instantiate"),
        ("What is the process of finding errors and bugs in a program to make it behave as expected?", "debugging")
        ]
        
        for question, answer_key in questions:
            client_socket.sendall(question.encode())
            answer = client_socket.recv(1024)
            if answer.decode() == str(answer_key):
                print("Correct!\n")
                score = score + 10
            else:
                print("Not Correct...\n")

        out = "EXIT"
        out = str(out)
        client_socket.sendall(out.encode())
    
    response = client_socket.recv(1024)
    if response.decode() == "Done":
        asd = str(score)
        return asd

def English():
    score = 0    
    Instructions="Instructions\n-You will be given 3 Questions during your Quiz Answer them one by one.\n-Each Question holds 10 marks\n"
    client_socket.sendall(Instructions.encode())

    response = client_socket.recv(1024)
    
    if response.decode() == "Okay":
        questions = [
        ("Question 1: What is the past tense of 'eat'?", "ate"),
        ("Question 2: What is the plural form of 'child'?", "children"),
        ("Question 3: What is the comparative form of 'good'?", "better")
        ]

        for question, answer_key in questions:
            client_socket.sendall(question.encode())
            answer = client_socket.recv(1024)
            if answer.decode() == str(answer_key):
                print("Correct!\n")
                score = score + 10
            else:
                print("Not Correct...\n")

        out = "EXIT"
        out = str(out)
        client_socket.sendall(out.encode())
    
    response = client_socket.recv(1024)
    if response.decode() == "Done":
        asd = str(score)
        return asd
    

# Choose the Quiz
def Quiz(request):
    if request == "1":
        Score = Mathematics()
        return Score
    
    elif request == "2":
        Score = Programming()
        return Score
    elif request == "3":
        Score = English()
        return Score

# Define the sub-server address and port
SUB_SERVER_HOST = '127.0.0.1'
SUB_SERVER_PORT = 54321

# Create a socket object
sub_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
sub_server_socket.bind((SUB_SERVER_HOST, SUB_SERVER_PORT))

# Listen for incoming connections
sub_server_socket.listen(5)

print("Sub-Server is listening for connections...")

while True:
    # Accept incoming connections
    client_socket, client_address = sub_server_socket.accept()
    print(f"Connection established with {client_address}")

    while True:
        # Receive data from the client
        data = client_socket.recv(1024)
        if not data:
            break
        data=data.decode()

        Final = Quiz(data)
        Final = str(Final)
        # Process the data (in this case, just echo back)
        client_socket.sendall(Final.encode())


    # Close the connection
    client_socket.close()
