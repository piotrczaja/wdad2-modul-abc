#!/usr/bin/python3

from datetime import datetime

from lib.modulA.modula import modulA
from lib.modulB.modulb import modulB
from lib.modulC.modulc import modulC

now = datetime.now()

def timestampwykonania():
    godzina = now.strftime("%H:%M:%S")
    data = now.strftime("%m.%d.%Y")
    print("Sktypt wykonany: ", data, " o godzinie ", godzina)

modulA()
modulB()
modulC()
timestampwykonania()


