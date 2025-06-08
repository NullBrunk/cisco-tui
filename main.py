#!/usr/bin/env python3

from cli.parser import parse
from socket import socket

def main():
    ip, port = parse()


if __name__ == "__main__":
    main()