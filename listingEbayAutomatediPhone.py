import os, re, webbrowser, time, pyautogui, pyperclip
from ebaylogindispatch import login

os.chdir('D:\Dropbox\ebayPythonScripts')
# directory for single images
dirSingImages = 'D:\\Dropbox\Business\Sublimation\\to do\\ebaySingleiPhone'
# directory for main images
dirMainImage = 'D:\\Dropbox\Business\Sublimation\\to do\\eBaySingleForMainiPhone'

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

# iPhone Phone Cases & Covers
templateLink = 'https://bulksell.ebay.co.uk/ws/eBayISAPI.dll?SingleList&sellingMode=AddItem&templateId=5045237010'

# iPhone Flip Wallets
#templateLink = ''

# Samsung Phone Cases & Covers
#templateLink = ''

# Single image, iPhone, Samsung, Huwawei, XIAOMI?
#templateLink = ''

#Regex for phone case image from reading file imageRegex

# Loop through list
# For every main file in the list start a listing process
loginIndex = 0

for files in (mainList):
    #if (loginIndex % 5 == 0):
    #    login()
        
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
    time.sleep(15)
    pyautogui.moveTo(640, 1410, duration=0.5) #edit variations
    pyautogui.click()
    time.sleep(8)
    pyautogui.moveTo(750, 365, duration=0.5) #edit
    pyautogui.click()
    time.sleep(8)
    
    for codes in (phoneCaseImagesList):
        pyautogui.moveTo(200, 780, duration=0.5)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.typewrite(codes)
        pyautogui.press('enter')
        time.sleep(0.5)
        
    pyautogui.moveTo(1856, 514, duration=0.5)
    pyautogui.click() # remove X from phone case image variations
    pyautogui.moveTo(280, 1142, duration=0.5)
    pyautogui.click() # update variations
    pyautogui.moveTo(1020, 380, duration=1)
    pyautogui.click() # add rows automatically

    time.sleep(4)

    # Add images
    pyautogui.moveTo(1854, 920, duration=1)
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
    pyautogui.moveTo(800, 1100, duration=1)
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
    coreMainFilePath = 'D:\Dropbox\Business\Sublimation\to do\eBaySingleForMainiPhone\\'
    addMainFilePath = 'to do\eBaySingleForMainiPhone'
    MainFileName = str(files) + 'MainIPHONE.jpg'
    
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
    time.sleep(2)
    pyautogui.scroll(-1000)
    
    pyautogui.moveTo(440, 1335, duration=1)
    pyautogui.click()
    time.sleep(2)
    pyautogui.press('down')
    time.sleep(2)
    
    pyautogui.scroll(-1000)
    time.sleep(2)
    # SINGLE IMAGES
    coreSingleFilePath = 'D:\Dropbox\Business\Sublimation'
    addSingleFilePath = 'to do\ebaySingleiPhone'
    
    y = 890

    for codes in (phoneCaseImagesList):
        pyautogui.moveTo(158, y, duration=1)
        pyautogui.click()

        pyautogui.moveTo(1854, 956, duration=1)
        pyautogui.click()

        pyautogui.moveTo(800, 1100, duration=1)
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
        
        pyautogui.typewrite(codes + 'SingleIPHONE.jpg')
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(2)
        
        y += 74

    pyautogui.scroll(-1000)
    
    # SELECT ALL
    pyautogui.moveTo(144, 1554, duration=1)
    pyautogui.click()
    
    # ENTER PRICE FOR ALL
    pyautogui.moveTo(276, 1440, duration=1)
    pyautogui.click()
    pyautogui.typewrite('4.69')
    pyautogui.moveTo(680, 1730, duration=1)
    pyautogui.click()
    time.sleep(1)
    
    # ENTER QUANTITY FOR ALL
    pyautogui.moveTo(640, 1430, duration=1)
    pyautogui.click()
    pyautogui.typewrite('2')
    pyautogui.moveTo(1040, 1730, duration=1)
    pyautogui.click()
    time.sleep(1)
    
    # EAN
    pyautogui.moveTo(1280, 1645, duration=1)
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

    time.sleep(1)        
    pyautogui.scroll(-2000)
    
    # Submiting & Close by ctrl w
    pyautogui.moveTo(230, 1700, duration=1)
    pyautogui.click()

    time.sleep(30)
    # Accept recommend item specifics
    pyautogui.scroll(-3000)
    pyautogui.moveTo(1370, 1400, duration=1)
    pyautogui.click()
    time.sleep(1)
    
    time.sleep(12)
    pyautogui.scroll(-20000)
    pyautogui.moveTo(350, 1620, duration=1)
    pyautogui.click()
    time.sleep(20)
    
    pyautogui.hotkey('ctrl', 'w')
    loginIndex += 1
