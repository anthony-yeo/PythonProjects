import webbrowser, sys, pyperclip

sys.argv # ['mapit.py', '123', 'Brown', St.']

#Check if command line arguments were passed
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:]) # begins at index 1 and then goes to the end of the array
else:
    address = pyperclip.paste() #takes whatever is in the clipboard and puts into 'address' variable

# https://www.google.com/maps/place/<ADDRESS>
webbrowser.open('https://www.google.com/maps/place/' + address)


""" Bat File
@py.exe E:\Python\Projects\mapit.py %*

"""
