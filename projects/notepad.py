import os 
import time 
def  open_notepad():
    time.sleep(1)
    print("openning notepad ..")
    os.system('notepad')

def  close_notepad():
    time.sleep(0.9)
    print("closing notepad ..")
    os.system('taskkill /im  notepad.exe')
