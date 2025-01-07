import socket

# Define the main server address and port
MAIN_SERVER_HOST = '127.0.0.1'
MAIN_SERVER_PORT = 12345

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the main server
client_socket.connect((MAIN_SERVER_HOST, MAIN_SERVER_PORT))

while True:
    # Send data to the main server
    test = input("\n1.Mathematics\n2.Programming\n3.English\nChoose the Test: ")
    client_socket.sendall(test.encode())

    # Receive response from the main server
    response = client_socket.recv(1024)
    print("Response: ", response.decode())

    message = "Okay"
    client_socket.sendall(message.encode())

    #comunicating for questions
    while True:    
        question = client_socket.recv(1024)
        question = question.decode()
        if question == "EXIT":
            break
        else:
            print(question)
            answer = input("Your answer: ")
            print("\n")
            client_socket.sendall(answer.encode())

    message = "Done"
    client_socket.sendall(message.encode())
    
    # for printing Score
    if test == "1":    
        marks = client_socket.recv(1024)
        marks = marks.decode()
        print("Total Score For Mathematics Test is : ",marks,"/30")
    elif test == "2":    
        marks = client_socket.recv(1024)
        marks = marks.decode()
        print("Total Score For Programming Test is : ",marks,"/30")
    elif test == "3":    
        marks = client_socket.recv(1024)
        marks = marks.decode()
        print("Total Score For English Test is : ",marks,"/30")
    


    choose = input("Press 1 to choose again else type 0: ")
    if choose == "1":
        print("\n\n")
    else:
        print("------------------------------BYE------------------------------")
        break
# Close the connection
client_socket.close()
