import socket

HOST = "localhost"
PORT = 9999
message = "test message"


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(bytes(message.encode()), (HOST, PORT))
received = sock.recv(1024).decode()
sock.close()

print("Sent: " + message)
print("Received: " + str(received))

