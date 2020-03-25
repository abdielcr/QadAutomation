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

#Function Insert data on ERP items
def detallesUsuario(i):
    #Open Source Data
    document = xlrd.open_workbook('c:/Users/fevisarpa/Desktop/concentrado.xlsx',"r")

    sheet = document.sheet_by_index(0)
    #disponibilidad item
    pyautogui.click(x=273,y=159, clicks=1,  button='left')

    #Reorden punto item
    pyautogui.click(x=1455,y=231, clicks=2,  button='left')
    a5 = sheet.cell_value(rowx=i,colx=5)
    pyautogui.typewrite(str(a5))
    pyautogui.press('left')
    pyautogui.press('left')
    pyautogui.press('del')
    pyautogui.press('del')
  
    pyautogui.click(x=1504,y=258, clicks=2,  button='left')
    a6 = sheet.cell_value(rowx=i,colx=6)
    pyautogui.typewrite(str(a6))

    pyautogui.press('left')
    pyautogui.press('left')
    pyautogui.press('del')
    pyautogui.press('del')

    #Inventario seguridad item
    pyautogui.click(x=1517,y=282, clicks=2,  button='left')
    a7 = sheet.cell_value(rowx=i,colx=7)
    pyautogui.typewrite(str(a7))


    pyautogui.press('left')
    pyautogui.press('left')
    pyautogui.press('del')
    pyautogui.press('del')

    #Unidad Orden item
    pyautogui.click(x=1528,y=330, clicks=2,  button='left')
    a8 = sheet.cell_value(rowx=i,colx=8)
    pyautogui.typewrite(str(a8))
    pyautogui.press('left')
    pyautogui.press('left')
    pyautogui.press('del')
    pyautogui.press('del')
    
    document.release_resources()
    del document
   
   