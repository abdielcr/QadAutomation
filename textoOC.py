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

#Function insert TextoOC on ERP items    
def textoOC():
    pyautogui.click(481,164, clicks=1,  button='left')
    pyautogui.click(473,221, clicks=1,  button='left')
    pyautogui.typewrite('SOLICITUD GENERADA AUTOMATICAMENTE POR PUNTO DE REORDEN.')
   

