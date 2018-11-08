import os, re, webbrowser, time, pyautogui, pyperclip
from ebaylogindispatch import login

os.chdir('D:\Dropbox\ebayPythonScripts')
# directory for single images
dirSingImages = 'D:\\Dropbox\Business\Sublimation\\to do\\ebaySingleSamsung\\5-8'
# directory for main images
dirMainImage = 'D:\\Dropbox\Business\Sublimation\\to do\\ebaySingleForMainSamsung'

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
templateLink = 'https://bulksell.ebay.co.uk/ws/eBayISAPI.dll?SingleList&sellingMode=AddItem&templateId=5331643010'

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
    time.sleep(15)
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
    time.sleep(0.5)
    pyautogui.typewrite(' #5-8')
    
    # Add variations, loop through list of images, for Samsung some files will be moved to limit variations
    time.sleep(10)
    pyautogui.moveTo(575, 1310, duration=1.5) #edit variations
    pyautogui.click() #
    time.sleep(15)
    pyautogui.moveTo(684, 330, duration=1.5) #edit
    pyautogui.click() #
    time.sleep(10)
    
    for codes in (phoneCaseImagesList):
        pyautogui.moveTo(184, 696, duration=0.5)
        pyautogui.click() #
        time.sleep(0.5)
        pyautogui.typewrite(codes)
        pyautogui.press('enter')
        time.sleep(0.5)
        
    pyautogui.moveTo(1844, 465, duration=0.5) #
    pyautogui.click() # remove X from phone case image variations
    pyautogui.moveTo(200, 966, duration=0.5) #
    pyautogui.click() # update variations
    pyautogui.moveTo(1100, 1060, duration=1) #ok
    pyautogui.click() # add rows automatically

    time.sleep(10)

    # Add images
    pyautogui.moveTo(1750, 890, duration=3) #
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
    pyautogui.moveTo(500, 780, duration=5) #
    pyautogui.click() # enter main image filename
    time.sleep(10)
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
    coreMainFilePath = 'D:\Dropbox\Business\Sublimation\to do\ebaySingleForMainSamsung\\'
    addMainFilePath = 'to do\ebaySingleForMainSamsung'
    MainFileName = str(files) + 'MainSamsung.jpg'
    
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
    
    pyautogui.moveTo(245, 1535, duration=1)
    pyautogui.click()
    time.sleep(2)
    pyautogui.press('down')
    time.sleep(2)
    
    pyautogui.scroll(-1000)
    time.sleep(6)
    # SINGLE IMAGES
    coreSingleFilePath = 'D:\Dropbox\Business\Sublimation'
    folderFilePath = 'to do\ebaySingleSamsung'
    subFolderFilePath = '5-8'
    y = 1060

    for codes in (phoneCaseImagesList):
        pyautogui.moveTo(158, 1340, duration=2)
        pyautogui.click() #
    
        pyautogui.moveTo(1760, 1400, duration=2)
        pyautogui.click() #

        pyautogui.moveTo(530, 785, duration=2)
        pyautogui.click() # enter single image filename
        time.sleep(2) #

        pyautogui.typewrite(coreSingleFilePath)
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(2)
        
        pyautogui.typewrite(folderFilePath)
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(2)
        
        pyautogui.typewrite(subFolderFilePath)
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(2)
        
        pyautogui.typewrite(codes + 'SingleSamsung.jpg')
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(2)
        
        y += 60

    pyautogui.scroll(-1000)
    pyautogui.scroll(-882)
    # SELECT ALL
    pyautogui.moveTo(132, 1385, duration=1)
    pyautogui.click() #
    
    # ENTER PRICE FOR ALL
    pyautogui.moveTo(250, 1280, duration=1)
    pyautogui.click() #
    pyautogui.typewrite('4.69')
    pyautogui.moveTo(620, 1540, duration=1)
    pyautogui.click() #
    time.sleep(1)
    
    # ENTER QUANTITY FOR ALL
    pyautogui.moveTo(600, 1280, duration=1)
    pyautogui.click() #
    pyautogui.typewrite('2')
    pyautogui.moveTo(940, 1540, duration=1)
    pyautogui.click() #
    time.sleep(1)
    
    # EAN
    pyautogui.moveTo(980, 1470, duration=1)
    pyautogui.click() #
    time.sleep(1)
    
    for i in range (1, 57):
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
            
    pyautogui.scroll(-2000)
    
    # Submiting & Close by ctrl w
    pyautogui.moveTo(200, 1730, duration=1)
    pyautogui.click() #ok

    time.sleep(30)
    pyautogui.scroll(-1500)
    pyautogui.moveTo(1100, 1620, duration=1)
    pyautogui.click()

    time.sleep(12)
    pyautogui.scroll(-10000)
    pyautogui.moveTo(240, 1750, duration=1)
    pyautogui.click() #
    time.sleep(12)
    
    #pyautogui.moveTo(1050, 880, duration=1)
    #pyautogui.click()
    time.sleep(5)
    pyautogui.hotkey('ctrl', 'w')
    loginIndex += 1
