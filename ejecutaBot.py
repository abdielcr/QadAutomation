#!/usr/bin/env/ python
'''EITDE'''
'''
@author    => AbdielC
@email     =>ascr3.1416@gmail.com
@lasUpdate => 3-20-2020
@version   => 1.0.1
'''
import pyautogui
import xlrd
from datetime import datetime
from finalFunciones import encontrar
from dias import diasEntrega
from iconoGuardar import guardarIcono
from detallesUsuario import detallesUsuario
from textoOC import textoOC
from defUsuario import defUsuario
from parteProveedor import parteProveedor
from nuevo import nuevo
from cerrarPestana import cerrarPestana

i= 0
inicio = datetime.now()

#Iterate n cases.
for i in range(23):
    encontrar(i)
    diasEntrega(i)
    detallesUsuario(i)
    textoOC()
    defUsuario(i)
    parteProveedor()
    nuevo(i)
    cerrarPestana()
    print(datetime.now()- inicio)
