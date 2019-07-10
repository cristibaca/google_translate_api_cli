#!/usr/bin/env python3

import argparse
import socket
import json


HOST = '127.0.0.1'
PORT = 65436

def main():
    parser = argparse.ArgumentParser(description="gltranslate 1.0: command line utility for translating text")
    requiredNamed = parser.add_argument_group('Parameters:')
    requiredNamed.add_argument("-f", dest='filename',  help="<filename>: path to input filename to be translated", required=True)
    requiredNamed.add_argument("-l", dest='language', help="<lang>: output language, can be one of 'en', 'it', or 'de' ", choices=['en', 'it', 'de'], required=True)
    args = parser.parse_args()

    arrayData = []

    print('Translating, please wait…')

    with open(args.filename) as file:
        array = file.read().splitlines()
        for text in array:
            arrayData.append({'text': text, 'language': args.language})

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.send(json.dumps(arrayData).encode('utf-8'))
        data = s.recv(1024)
        # print(data)
        for text in json.loads(data.decode('utf-8')):
            print(text)
if __name__ == '__main__':
    main()
