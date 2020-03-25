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

#Function insert User Update on ERP 
def defUsuario(i):
   #Open Source Data
   document = xlrd.open_workbook('c:/Users/fevisarpa/Desktop/concentrado.xlsx',"r")
   sheet = document.sheet_by_index(0)
   
   pyautogui.click(559,161, clicks=1,  button='left')
   pyautogui.click(326,210,clicks=1,  button='left')
   pyautogui.typewrite('JMMM')
   pyautogui.PAUSE = 2.0
   pyautogui.click(x=1132, y=210)
   pyautogui.typewrite('SI')

   pyautogui.click(x=323, y=309,)
   a12 = sheet.cell_value(rowx=i,colx=12)
   pyautogui.typewrite(str(a12))
   pyautogui.click(1133,309,clicks=1,  button='left')
   
   document.release_resources()
   del document
    

