import socket


def create_socket():
    # Create a socket object for UDP
    return socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def send_data(sock, address, data):
    # Send data to the server
    sock.sendto(data.encode(), address)


def recv_data(sock):
    # Receive data from the server
    data, addr = sock.recvfrom(1024)
    return data.decode(), addr


def close_socket(sock):
    sock.close()


def main():
    s = create_socket()
    host = "localhost"
    port = 5000
    server_address = (host, port)

    try:
        data = "Hello, World!"
        send_data(s, server_address, data)

        received_data, addr = recv_data(s)
        print("Received data from server:", received_data)

    except Exception as e:
        print("An error occurred:", e)
    finally:
        close_socket(s)


if __name__ == "__main__":
    main()
