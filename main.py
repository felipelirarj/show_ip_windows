#Dependencies: py -m pip install requests

import requests
import socket
import platform   
import subprocess

import os


print('''

Sistem of check IPv4 invalid and IPv4 valid
Autor: Felipe Lira
''')

print('\n')

info = socket.gethostbyname_ex(socket.gethostname())


info = list(info)

list_info = len(info)

for item in range (list_info):
    hostname = info[0]
    ip = info[2]
    


print(f"Hostname: {hostname}")

for address in ip:
    print(f"Address IPv4 Invalid: {address}")

ip_valid = requests.get('https://api.ipify.org/').text
print(f'Address IPv4 Valid: {ip_valid}')




print('\n')
pause_app=input('Press Any Key for finish script...')
