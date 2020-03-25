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

#Save Data
def guardarIcono():
    pyautogui.click(pyautogui.locateCenterOnScreen('guardar.png'))
    pyautogui.PAUSE = 1.0

  