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

#Function insert data on ERP
def nuevo(i):
    #Open Source Data
    document = xlrd.open_workbook('c:/Users/fevisarpa/Desktop/concentrado.xlsx',"r")
    sheet = document.sheet_by_index(0)
    
    pyautogui.click(x=473, y=133,clicks=1, interval=0.25, button='left')
    pyautogui.PAUSE = 5.0
    
    pyautogui.click(x=163, y=203,clicks=1, interval=0.25, button='left')
    a14 = sheet.cell_value(rowx=i,colx=14)
    
    pyautogui.typewrite(a14)
    pyautogui.click(x=305,y=203, clicks=1,  button='left')
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')


    pyautogui.click(x=1098,y=593, clicks=1,  button='left')
    document.release_resources()
    del document