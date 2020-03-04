#! python3

import pyautogui, time

pyautogui.PAUSE = 1 # every pyautogui funtion will wait 1 sec 
pyautogui.FAILSAFE = True # moving curson to top left of the screen will cause exception


print('How many listings to be revised?')
revisions = int(input())
print('This script will paste item description from clipboard ' + str(revisions) + ' times.')
time.sleep(5)

for i in range(revisions):
    time.sleep(1.5)
    pyautogui.click(1365, 1250)
    time.sleep(1.5)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    time.sleep(1.5)
    #pyautogui.typewrite(itemDescription)
    pyautogui.hotkey('ctrlleft', 'v')
    time.sleep(1.5)
    pyautogui.click(1495, 1515)
    time.sleep(20)

print('Script has finished')
time.sleep(6000)
