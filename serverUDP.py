import socketserver


class MyUDPHandler(socketserver.DatagramRequestHandler):
    def handle(self):
        message = self.request[0]
        print("Wrote: " + str(message))
        print(message)
        self.request[1].sendto(message.upper(), self.client_address)


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    server = socketserver.UDPServer((HOST, PORT), MyUDPHandler)
    server.serve_forever()
