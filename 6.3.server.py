import socket
import sys
import math

s = socket.socket()
port = 8080
s.bind(("", port))
s.listen(5)
print("\nServer address is 192.168.0.200")
print("Waiting for connections... ")
conn, addr = s.accept()
print(addr, "has connected to the server\n")
print("***Welcome to Online Calculator***")

def pilihan():
        print("\nPress 1 for Multiplication")
        print("Press 2 for Division")
        print("Press 3 for logarithmic")
        print("Press 4 to exit")

while True:
        pilihan()

        Input = input("Please enter your choice: ")

        if Input == '1':
                print("\nMULTIPLICATION")
                a = int(input("First number: "))
                b = int(input("Second number: "))
                print('{} x {} = '.format(a, b))
                print(a * b)
        elif Input == '2':
                print("\nDIVISION")
                a = int(input("First number: "))
                b = int(input("Second number: "))
                print('{} / {} = '.format(a, b))
                print(a/b)
        elif Input == '3':
                print("\nLOGARITHMIC")
                a = int(input("Please enter positive number only: "))
                print('log(number) = '.format(a))
                print(math.log(a))
        elif Input == '4':
                sys.exit()
        else:
                print("\n************Please enter a valid choice***********")
                continue
                
s.close
