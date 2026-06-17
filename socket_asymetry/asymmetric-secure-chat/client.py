import socket
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes


def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", 9999))
    #get_key = client_socket.recv(2048)
    #public_key = serialization.load_pem_public_key(get_key)
    #print(f"Клиент подключен к серверу, получен {public_key}")

    public_key_data = b''
    while True:
        chunk = client_socket.recv(1024)
        if not chunk:
            break
        public_key_data += chunk
        if b'-----END PUBLIC KEY-----' in public_key_data:
            break
    
    public_key = serialization.load_pem_public_key(public_key_data)
    

    while True:

        try:
            f = input("Введите сообщение: ")
            decode = public_key.encrypt(
                f.encode("utf-8"), 
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm = hashes.SHA256(), label = None))
            message_length = len(decode).to_bytes(4, byteorder="big")
            
            client_socket.send(message_length)
            client_socket.send(decode)
            response = client_socket.recv(1024)
            print(f"Ответ сервера: {response.decode("utf-8")}")
        except:
            break 
    client_socket.close()
start_client()

        