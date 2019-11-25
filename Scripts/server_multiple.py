#!/usr/bin/env python3

import socket
import sys
from _thread import *

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 12345        # Port to listen on (non-privileged ports are > 1023)

def handler_thread(conn, addr):
    global flag

    flag_connection = True;
    print('Connected by', addr)

    else:
        
        while (flag_connection):
            bytes = input('Server: ')
            conn.sendall(str.encode(bytes))

            data = conn.recv(1024)
            data_str = data.decode()

            if (data_str[0:4] == 'over'):
                conn.sendall(str.encode('Disconnected'))            
                flag_connection = False
                flag = False
                break

            print(f'Client {addr}: ', data_str)

        conn.close()

        print('Disconnected from:', addr)

        count -= 1

flag = True

def Main():
    global flag

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    while (flag):
        #print('I am the server')
        conn, addr = server_socket.accept()
        start_new_thread(handler_thread, (conn, addr))

if __name__ == '__main__':   
    Main()
