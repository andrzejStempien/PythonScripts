#! python3

import webbrowser, pyautogui, time

linkArchive = 'https://k2b-bulk.ebay.co.uk/ws/eBayISAPI.dll?SMDownloadRequest&ssPageName=STRK:ME:LNLK'

webbrowser.open(linkArchive)

# ebay
time.sleep(25)
pyautogui.moveTo(592, 812, duration=0.5)
pyautogui.click() #click file

pyautogui.moveTo(506, 1010, duration=0.5)
pyautogui.click() #click file

pyautogui.moveTo(392, 970, duration=0.5)
pyautogui.click() #click filedeleteDispatchToday

# save
pyautogui.moveTo(420, 1414, duration=0.5)
pyautogui.click() #click file

# download
time.sleep(15)
pyautogui.moveTo(232, 1126, duration=0.5)
pyautogui.click() #click file

pyautogui.moveTo(2240, 842, duration=1.5)
pyautogui.click() #click file
time.sleep(5)

# open

pyautogui.moveTo(208, 1738, duration=1)
pyautogui.click() #click file

# file

time.sleep(8)
pyautogui.moveTo(62, 92, duration=1)
pyautogui.click() #click file

# save as
time.sleep(2)
pyautogui.moveTo(68, 458, duration=1)
pyautogui.click() #click file

# dropbox
time.sleep(2)
pyautogui.moveTo(604, 314, duration=1)
pyautogui.click() #click file

# my python scripts
time.sleep(2)
pyautogui.moveTo(1050, 544, duration=1)
pyautogui.click() #click file

# detele & type
time.sleep(2)
pyautogui.typewrite(['delete'])
pyautogui.typewrite('DispatchToday')

# save
time.sleep(2)
pyautogui.moveTo(942, 840, duration=0.5)
pyautogui.click() #click file

# close excell
time.sleep(2)
pyautogui.moveTo(2836, 42, duration=0.5)
pyautogui.click() #click file

# close browser
time.sleep(2)
pyautogui.moveTo(2836, 12, duration=0.5)
pyautogui.click() #click file

# execute readingCSV
time.sleep(1)

#os.system('readingCSV.py')
#execfile('readingCSV.py')
