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

#Function search data on ERP items
def encontrar(i):
    #Open Source Data
    document = xlrd.open_workbook('c:/Users/fevisarpa/Desktop/concentrado.xlsx',"r")
    
    #Setting sheet
    items = document.sheet_by_index(0)
    
    #Setting rows   
    row_data = items.nrows

    #Printing number of rows found    
    print(row_data)
    
    #---Section Insert code---
    #Renamen sheet access
    sheet = document.sheet_by_index(0)
    pyautogui.click(x=258,y=127, clicks=1,  button='left')
    
    pyautogui.press('del')
    pyautogui.press('del')
    pyautogui.press('del')
    pyautogui.press('del')
    pyautogui.press('del')
    pyautogui.press('del')
    pyautogui.press('del')
    pyautogui.press('del')
    pyautogui.press('del')
    pyautogui.press('del')
    pyautogui.press('del')
    pyautogui.press('del')
    pyautogui.press('del')
    pyautogui.press('del')
    pyautogui.press('del')
    pyautogui.press('del')
    
    #Read A2 cell xls sheet
    a2 = sheet.cell_value(rowx=i,colx=1)
    pyautogui.typewrite(a2)

    #Click on search Point
    pyautogui.click(pyautogui.locateCenterOnScreen('busca.png'))
    
    #Double click on item
    pyautogui.click(x=316,y=164, clicks=2,  button='left')
    pyautogui.PAUSE = 4.0
    document.release_resources()
    del document

    