"""
dient als sender des RCSwitch, um die Funksteckdosen zu steuern
wird von Node Red aus aufgerufen
benötigt Python 3!

Autor: AL
Version 16.08.20
"""

from rpi_rf import RFDevice # Libary für rcswitch
import sys  # Variable Werte koennen in Programm uebertragen werden

rfdevice = RFDevice(17) # GPIO pi
rfdevice.enable_tx()

state = "Aoff" # default wert
try:
    state = sys.argv[1] # versucht uebertragenen wert zu lesen, sonst default wert
except:
    state = "Moff"
#input("Xon or Xoff (A,B,C,D): ")

for a in range(1,4): # wiederholt den zyklus 3x um sicher zu gehen
    print ("durchlauf: ",a)
    if state == "Aoff":
        print("A aus")
        rfdevice.tx_code(4118572, 3, 101)
    
    elif state == "Aon":
        print("A an")
        rfdevice.tx_code(3151788, 3, 101)
    
    elif state == "Boff":
        print("B aus")
        rfdevice.tx_code(3995205, 3, 101)
    
    elif state == "Bon":
        print("B an")
        rfdevice.tx_code(4168949, 3, 101)
        
    elif state == "Moff":
        print("M aus")
        rfdevice.tx_code(3522578, 3, 101)
    
    elif state == "Mon":
        print("M an")
        rfdevice.tx_code(4118562, 3, 101)
"""
    elif state == "Coff":
    #    rfdevice.tx_code(, 3, 101)
    elif state == "Con":
    #    rfdevice.tx_code(, 3, 101)
    elif state == "Don":
    #    rfdevice.tx_code(, 3, 101)
    elif state == "Don":
    #    rfdevice.tx_code(, 3, 101)
"""
print("end")
