import socket
import threading

nickname = input('pick a nickname: ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('127.0.0.1', 55000))


def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'nick':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print('error')
            client.close()
            break


def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()