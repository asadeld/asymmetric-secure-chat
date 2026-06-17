import socket
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes


key_privat = rsa.generate_private_key(key_size=2048, public_exponent=65537)
key_public = key_privat.public_key()

#сереализация
public_ser = key_public.public_bytes(encoding= serialization.Encoding.PEM, format= serialization.PublicFormat.SubjectPublicKeyInfo)

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 9999))
    server_socket.listen(1)
    print("Сервер запущен")
    con, addr = server_socket.accept()
    con.send(public_ser)

    while True:
        try:

            f = con.recv(4)

            message_length = int.from_bytes(f, byteorder="big")
            print(message_length)

            encrypted_data = b''
            while len(encrypted_data) < message_length:
                chunk = con.recv(min(message_length - len(encrypted_data), 1024))
                if not chunk:
                    raise ConnectionError("Соединение разорвано")
                encrypted_data += chunk
            

            decode = key_privat.decrypt(
                encrypted_data, 
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm = hashes.SHA256(), label = None))
            print(f"Получено сообщение: {decode.decode('utf-8')}")
            con.send(b"Message")
        except Exception as e:
            print(e)
            break
    con.close() 
    server_socket.close()
start_server()

        