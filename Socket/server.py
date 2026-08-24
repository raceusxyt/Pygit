import socket

s = socket.socket()
print("Socket Created")

s.bind(("localhost", 9999))
print("Socket binded to 9999")

s.listen(3)
print("Waiting for connections")

while True:
    c, addr =s.accept()
    name = c.recv(1024).decode()
    print("Connected with", addr, "as", name)

    c.send(bytes("Welcome to Alicia", "utf-8"))

    c.close()