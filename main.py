#! /usr/bin/python


import socket
import argparse

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 5555  # The port used by the server


def main(args):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((args.target, args.port))
        s.sendall(b"Hello, world")
        data = s.recv(1024)

    print(f"Received {data!r}")


if _name_ == '_main_':
    parser = argparse.ArgumentParser(description='Kilnet TCP')
    parser.add_argument('-t', '--target')
    parser.add_argument('-p', '--port', type=int, default=5555)

    args = parser.parse_args()
    main(args)