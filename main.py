import pyautogui
import time

def main():
    
    
    #Timer
    
    for i in range(10):
        print("Sample")
        time.sleep(0.1)
        currentMouseX, currentMouseY = pyautogui.position()
        pyautogui.moveTo(currentMouseX-10, currentMouseY+40)


    


    

main()