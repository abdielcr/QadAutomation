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

#Function insert dias de entrega on ERP items
def diasEntrega(i):
    
    #Open Source Data
    document = xlrd.open_workbook('c:/Users/fevisarpa/Desktop/concentrado.xlsx',"r")
    
    #Setting sheet
    sheet = document.sheet_by_index(0)
    pyautogui.click(x=169, y=161)
    pyautogui.click(x=1147,y=258,clicks=1, interval=0.25, button='left')
    a4 = sheet.cell_value(rowx=i,colx=4)
    pyautogui.typewrite(str(a4))
    pyautogui.press('left')
    pyautogui.press('left')
    pyautogui.press('del')
    pyautogui.press('del')
    document.release_resources()
    del document
  

    