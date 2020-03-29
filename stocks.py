import pyautogui, tkinter, pyperclip, webbrowser, time
import openpyxl
import os

#initialize excel file
os.chdir('E:\Python\Projects')
wb = openpyxl.load_workbook(filename = 'test.xlsx')

"""
#keep out of loop
low = []
high = []
current = []
"""

#loop to fill init list
loop = True
tickList = []
while(loop):
    #--------CAPITALIZE INPUT
    ticker = input("Input the ticker(s) you want to search (input \"ZZZZ\" to end list):")
    if (ticker == "ZZZZ"):
        break;
    else:
        tickList.append(ticker)
#print(tickList)
        
#ticker = input("Input the ticker you want to search:")
r = 1
for i in tickList:
    #-Beginning of loop with initial list
    webbrowser.open('https://www.finance.yahoo.com/quote/' + i)
    pyautogui.moveTo(546, 726)#--------------- 1080 x 1920
    time.sleep(5.2) #lets the webpage load

    #pyautogui.drag(-120, 0, .5, button='left')
    pyautogui.click(clicks = 3)
    pyautogui.hotkey('ctrl', 'c') #takes the hi lo and puts into the clipboard

    hilow = pyperclip.paste()
    print(hilow)

    #498 406
    
    split = hilow.split("-")
    #print(split[0].strip() + " " + split[1].strip())


    pyautogui.moveTo(498, 406)#------------------1080 x 1920
    #pyautogui.drag(-180, 0, .5, button = 'left')
    pyautogui.click(clicks = 3)
    pyautogui.hotkey('ctrl', 'c')

    price = pyperclip.paste()
    barePrice = price.replace("-", " ")
    barePrice = price.replace("+", " ")
    priceSplit = barePrice.split(" ")
    print(priceSplit)
    #low.append(split[0].strip())
    #high.append(split[1].strip())

    #high low count
    #count = 0
    
    #row count

    #make loop for coloumn/row and make loop for hi low list
    os.chdir('E:\Python\Projects')
    wb = openpyxl.load_workbook(filename = 'test.xlsx')
    ws = wb.active
    ws.cell(row = r, column = 1).value = str(tickList[r-1])
    ws.cell(row = r, column = 2).value = float(priceSplit[0])
    ws.cell(row = r, column = 3).value = float(split[0].strip())
    ws.cell(row = r, column = 4).value = float(split[1].strip())
    wb.save('test.xlsx')
    
    r += 1
    
os.system("taskkill /im firefox.exe /f")





