# open port 5000 to recieve client message

import socket


def create_udp_server(host, port):
    """
    Create a UDP server.
    """
    # Create a socket object for UDP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the address and port
    server_socket.bind((host, port))
    print(f"UDP server up and listening on {host}:{port}")

    return server_socket


def listen_for_messages(server_socket):
    """
    Listen for messages and respond.
    """
    while True:
        # Receive message
        data, addr = server_socket.recvfrom(1024)  # buffer size is 1024 bytes
        print(f"Received message: {data.decode()} from {addr}")

        # Send a response back to the client
        response = "ACK: " + data.decode()
        server_socket.sendto(response.encode(), addr)


def main():
    host = "127.0.0.1"
    port = 5000

    server_socket = create_udp_server(host, port)
    try:
        listen_for_messages(server_socket)
    except KeyboardInterrupt:
        print("\nServer is shutting down.")
    finally:
        server_socket.close()


if __name__ == "__main__":
    main()
