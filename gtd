#!/usr/bin/env python3

import socket

import json

import subprocess

import daemon

import sys

import os

from ratelimit import limits, RateLimitException

HOST = '127.0.0.1'
PORT = 65436

QUERIES_PER_SEC = os.environ.get("QUERIES_PER_SEC", 10)

@limits(calls=int(QUERIES_PER_SEC), period=1)
def run_translator(text, targetLang):
        p = subprocess.Popen(["./translator", text, targetLang], stdout=subprocess.PIPE, bufsize=1)
        output = p.communicate()[0].decode("utf-8")
        p.kill()
        return  output


def run_app():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            translations_array = []
            conn, addr = s.accept()
            with conn:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    response = json.loads(data.decode('utf-8'))
                    for recv_data in response:
                        try:
                            translation = run_translator(recv_data['text'], recv_data['language'])
                            translations_array.append(translation)
                        except RateLimitException:
                            print("Max requests limit exceeded")
                    conn.sendall(json.dumps(translations_array).encode('utf-8'))

def run():
    with daemon.DaemonContext(working_directory='.', stdout=sys.stdout):
        run_app()


if __name__ == "__main__":
    run()
