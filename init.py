import pyautogui, tkinter, pyperclip, webbrowser, time
from openpyxl import Workbook

ticker = input("Input the ticker you want to search:")

webbrowser.open('https://www.finance.yahoo.com/quote/' + ticker)

pyautogui.moveTo(546, 726)

time.sleep(4) #lets the webpage load

pyautogui.drag(-120, 0, .5, button='left')
pyautogui.hotkey('ctrl', 'c')

hilo = pyperclip.paste()
#print(hilo)

split = hilo.split("-")
print(split[0].strip())
