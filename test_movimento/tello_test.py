from tello import Tello
import sys
from datetime import datetime
import time

start_time = str(datetime.now())

tello = Tello()
file_comandi = open("comandi.txt", "r")
comandi = file_comandi.readlines()
for comando_corrente in comandi:
    if comando_corrente != '' and comando_corrente != '\n':
        comando_corrente = comando_corrente.rstrip()

        if comando_corrente.find('delay') != -1:
            sec = float(comando_corrente.partition('delay')[2])
            print('delay %s' % sec)
            time.sleep(sec)
            pass
        else:
            tello.send_command(comando_corrente)

log = tello.get_log()

out = open('log/' + start_time + '.txt', 'w')
for stat in log:
    stat.print_stats()
    str = stat.return_stats()
    out.write(str)