#! python3

import openpyxl, pyautogui, os, pyperclip, time
pyautogui.PAUSE = 1 # every pyautogui funtion will wait 1 sec 
pyautogui.FAILSAFE = True # moving curson to top left of the screen will cause exception

os.chdir('D:\Dropbox\ebayPythonScripts') # setup current working directory

# Search directory for file with .txt extension
for files in (os.listdir('.')):
    if not (files.endswith('.txt') and files.startswith('filesToBePrinted')):
        continue
    txtFile = os.path.basename(files)

print('\n Printing file: ' + txtFile + '.\n')

printingListFile = open(os.getcwd() + '\\' + txtFile)
print('\n Printing from file path: ' + printingListFile.name + '.\n')

printingListFileContent = printingListFile.readlines()

for i in range(0, len(printingListFileContent)):
    print('\n Printing file from ' + str(printingListFileContent[i]) + '...\n')

    # click on desktop
    #pyautogui.click(1264, 64) # desktip click
    #pyautogui.click(1264, 64) # unselecting
    
    # copy filepath to clipboard
    #pyperclip.copy

    # cmd + r /run and paste file to command to open
    #pyautogui.hotkey('winleft', 'r')
    #pyautogui.moveTo(417, 86, duration=1)
    #pyautogui.click()
    
    # paste
    #pyautogui.press('backspace')
    #pyautogui.hotkey('ctrlleft', 'v')
    #time.sleep(1)
    
    # enter
    #pyautogui.typewrite(['enter'])

    os.startfile('D:\Dropbox\Business\Sublimation\\3. All models ready to print\\' + str(printingListFileContent[i]).strip('\n'))
    time.sleep(1)
    
    #printing setup
    pyautogui.moveTo(46, 70, duration=0.1)
    pyautogui.click() #click file

    pyautogui.moveTo(134, 521, duration=0.1) # move curson to print

    pyautogui.moveTo(792, 323, duration=0.1)
    pyautogui.click()   #click page setup

    pyautogui.moveTo(1330, 848, duration=0.1)
    pyautogui.click()   #click portrait

    pyautogui.moveTo(1512, 1080, duration=0.1)
    pyautogui.click()   #click adjust size 100%

    pyautogui.moveTo(1733, 1290, duration=0.1)
    pyautogui.click()   #click ok
    
    # print
    pyautogui.hotkey('ctrlleft', 'p')
    time.sleep(0.1)


    pyautogui.moveTo(528, 788, duration=0.1) # print button
    pyautogui.click()

    # close
    pyautogui.moveTo(2825, 14, duration=0.1) # X closing
    pyautogui.click()

    # wait second after closing
    print('Waiting a second to print next file\n')
    time.sleep(0.1)

print('\n All files were printed, total of ' + str(len(printingListFileContent)) + ' files. \n')

# moving printed file
shutil.move('D:\Dropbox\ebayPythonScripts\ProcessedToList\\' + printingListFile.name + '.txt', 'D:\Dropbox\ebayPythonScripts\ProcessedToList\\' + printingListFile.name + '.txt')
