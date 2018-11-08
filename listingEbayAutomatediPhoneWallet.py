import os, re, webbrowser, time, pyautogui, pyperclip
from ebaylogindispatch import login

os.chdir('D:\Dropbox\ebayPythonScripts')
# directory for single images
dirSingImages = 'D:\\Dropbox\Business\Sublimation\\to do\\ebaySingleWalletiPhone'
# directory for main images
dirMainImage = 'D:\\Dropbox\Business\Sublimation\\to do\\eBaySingleWalletForMainiPhone'

os.chdir(dirMainImage)

mainList = []
mainImageRegex = re.compile(r'((\w)+)(\d\d)')               

# Loop through Mains and find codes
for files in (os.listdir(dirMainImage)):
    
    if not (files.endswith('.jpg')):
        continue
    #print(files)
    try:
        matchMainImage = mainImageRegex.search(files)
        #print(matchMainImage.group())
        mainList.append(matchMainImage.group())
    except:
        matchMainImage = None
        
mainList.sort()
#print(mainList)

# iPhone Flip Wallets
templateLink = 'https://bulksell.ebay.co.uk/ws/eBayISAPI.dll?SingleList&sellingMode=AddItem&templateId=5318432010'




#Regex for phone case image from reading file imageRegex

# Loop through list
# For every main file in the list start a listing process
loginIndex = 0

for files in (mainList):
##    if (loginIndex % 5 == 0):
##        login()
        
    # Regex search for images that match current main image, adding to the list 
    phoneCaseImagesList = []
    singleImageRegex = re.compile(files + '\d')

    # Loop through Mains and find codes
    for singles in (os.listdir(dirSingImages)):
        if not (singles.endswith('.jpg')):
            continue
        try:
            matchSingleImage = singleImageRegex.search(singles)
            #print(matchSingleImage.group())
            phoneCaseImagesList.append(matchSingleImage.group())
        except:
            matchMainImage = None        
            phoneCaseImagesList.sort()
    #print(phoneCaseImagesList)

    # Open browser, login and close
    # approx 1 min to complete
    #login()
    #time.sleep(3)
    # Start, open template    
    webbrowser.open(templateLink)
    time.sleep(12)
    #break

    # Listing scripting
    # Item title by openning text file from disk
    mainTitleFilePath = open(dirMainImage + '\\' + files + 'Title.txt')
    mainTitleFileContent = mainTitleFilePath.read()
    print(mainTitleFileContent)
    mainTitleFilePath.close()
    pyperclip.copy(mainTitleFileContent)
    time.sleep(10)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'v')
    
    # Add variations, loop through list of images, for Samsung some files will be moved to limit variations
    time.sleep(18)
    pyautogui.moveTo(640, 1410, duration=0.5) #edit variations
    pyautogui.click()
    time.sleep(10)
    pyautogui.moveTo(750, 360, duration=0.5) #edit
    pyautogui.click()
    time.sleep(10)

    pyautogui.moveTo(200, 780, duration=0.5)
    pyautogui.click()
    for codes in (phoneCaseImagesList):

        time.sleep(0.5)
        pyautogui.typewrite(codes)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(0.5)

    time.sleep(1)
    pyautogui.moveTo(1856, 518, duration=0.5)
    pyautogui.click() # remove X from phone case image variations
    pyautogui.moveTo(240, 1180, duration=0.5)
    pyautogui.click() # update variations
    pyautogui.moveTo(1020, 390, duration=1)
    pyautogui.click() # add rows automatically

    time.sleep(4)

    # Add images
    pyautogui.moveTo(1850, 900, duration=1)
    pyautogui.click() # add default main photo

##    pyautogui.moveTo(1280, 90, duration=1)
##    pyautogui.click() # edit path
##    time.sleep(1)
##    pyautogui.hotkey('ctrl', 'a')
##    pyautogui.press('backspace')
##    time.sleep(5)
##    pyautogui.typewrite('D:\Dropbox\Business\Sublimation\to do\eBaySingleForMain')
##    pyautogui.press('enter')
##    time.sleep(5)
    time.sleep(1)
    pyautogui.moveTo(830, 1100, duration=1)
    pyautogui.click() # enter main image filename
    time.sleep(1)
##    pyautogui.hotkey('tab')
##    time.sleep(0.5)
##    pyautogui.hotkey('tab')
##    time.sleep(0.5)
##    pyautogui.hotkey('tab')
##    time.sleep(0.5)
##    pyautogui.hotkey('tab')
##    time.sleep(0.5)
##    pyautogui.hotkey('tab')
##    time.sleep(0.5)

    # MAIN IMAGE
    coreMainFilePath = 'D:\Dropbox\Business\Sublimation\to do\\'
    addMainFilePath = 'to do\eBaySingleWalletForMainiPhone'
    MainFileName = str(files) + 'MainWALLET.jpg'
    
    pyautogui.typewrite(coreMainFilePath)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    
    pyautogui.typewrite(addMainFilePath)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    
    pyautogui.typewrite(MainFileName)
    time.sleep(2)
    pyautogui.press('enter')
    #pyautogui.moveTo(1750, 980, duration=1)
    #time.sleep(13) # drags main image file higher, used because of addition wallet pictures were present
    #pyautogui.dragRel(0, -200, duration=1)
    time.sleep(2)
    pyautogui.scroll(-1000)
    pyautogui.moveTo(440, 1330, duration=1)
    pyautogui.click()
    time.sleep(2)
    pyautogui.press('down')
    time.sleep(2)
    
    pyautogui.scroll(-1000)
    time.sleep(2)
    # SINGLE IMAGES
    coreSingleFilePath = 'D:\Dropbox\Business\Sublimation'
    addSingleFilePath = 'to do\ebaySingleWalletiPhone'
    
    y = 890

    for codes in (phoneCaseImagesList):
        time.sleep(1)
        pyautogui.moveTo(158, y, duration=1)
        pyautogui.click()

        pyautogui.moveTo(1854, 956, duration=1)
        pyautogui.click()

        pyautogui.moveTo(450, 1100, duration=1)
        pyautogui.click() # enter single image filename
        time.sleep(1)

        pyautogui.typewrite(coreSingleFilePath)
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(2)
        
        pyautogui.typewrite(addSingleFilePath)
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(2)
        
        pyautogui.typewrite(codes + 'SingleIPHONEWallet.jpg')
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(2)
        
        y += 74

    pyautogui.scroll(-1000)
    pyautogui.scroll(-882)
    # SELECT ALL
    pyautogui.moveTo(144, 1064, duration=1)
    pyautogui.click()
    
    # ENTER PRICE FOR ALL
    pyautogui.moveTo(260, 950, duration=1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.typewrite('8.49')
    pyautogui.moveTo(680, 1240, duration=1)
    pyautogui.click()
    time.sleep(1)
    
    # ENTER QUANTITY FOR ALL
    pyautogui.moveTo(580, 950, duration=1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.typewrite('2')
    pyautogui.moveTo(1030, 1232, duration=1)
    pyautogui.click()
    time.sleep(1)
    
    # EAN
    pyautogui.moveTo(1200, 1170, duration=1)
    pyautogui.click()
    time.sleep(1)
    
    for i in range (1, 91):
        pyautogui.typewrite('Does not apply')

        time.sleep(0.5)
        pyautogui.hotkey('tab')
        time.sleep(0.5)
        pyautogui.hotkey('tab')
        time.sleep(0.5)
        pyautogui.hotkey('tab')
        time.sleep(0.5)
        pyautogui.hotkey('tab')
        time.sleep(0.5)
        pyautogui.hotkey('tab')
        time.sleep(0.5)
        pyautogui.hotkey('tab')
        time.sleep(0.5)
        pyautogui.hotkey('tab')
        time.sleep(0.5)
            
    pyautogui.scroll(-2000)
    
    # Submiting & Close by ctrl w
    pyautogui.moveTo(200, 1700, duration=1)
    pyautogui.click()

    time.sleep(30)
    pyautogui.scroll(-2500)
    pyautogui.moveTo(1390, 1680, duration=1)
    pyautogui.click()

    time.sleep(5)
    pyautogui.scroll(-20000)
    pyautogui.moveTo(260, 1620, duration=1)
    pyautogui.click()
    time.sleep(20)

    pyautogui.hotkey('ctrl', 'w')
    #pyautogui.hotkey('ctrl', 'w')
    #loginIndex += 1
