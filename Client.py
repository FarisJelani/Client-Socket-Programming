import socket

def main():
    # Server information
    server_address = "izani.synology.me"
    server_port = 8443

    # Your unique ID
    your_id = "2023149293"

    # Create a socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((server_address, server_port))
        print("Connected to the server")

        # Send your ID to the server
        client_socket.sendall(your_id.encode())
        print(f"Sent ID to the server: {your_id}")

        # Receive and print the server response
        server_response = client_socket.recv(1024).decode()
        print(f"Server response: {server_response}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the socket
        client_socket.close()
        print("Connection closed")

if __name__ == "__main__":
    main()
