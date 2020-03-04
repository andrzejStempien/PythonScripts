#!python3

# Skrypt przeszukuje wybrany katalog odnajduje contact sheets stworzone
# w photoshopie i kody obrazkow, nastepnie zmienia nazwe contact sheets
# tak by pasowaly do kodow obrazkow z ktorych zostaly stworzone

import os, re, shutil

#dir to rename Main iPhone files
#os.chdir('D:\\to do\\eBaySingleForMainiPhone\\4')

#dir to rename Main Samsung files
#os.chdir('D:\\to do\\ebaySingleForMainSamsung\\4')

#dir to rename Main iPhone Wallets files
#os.chdir('D:\\to do\\eBaySingleWalletForMainiPhone\\4')

currentPath = os.path.abspath(os.getcwd())

contactSheetList = []
imageCodesList = []
imageCodes = []
notContactSheetFilesList = []

imageRegex = re.compile(r'(\w\w\w\d\d)(\d)')               

#Search for Contact Sheets and add them to the list
for files in (os.listdir('.')):
    if (files.startswith('ContactSheet')):
            contactSheetList.append(files)
    #print(files)
contactSheetList.sort()

#print(contactSheetList)
        
#Search for codes and add them to the list if code is not on the list

# Creates list of files that are not contact sheets
for notContactSheet in (os.listdir('.')):
    if(notContactSheet.startswith('ContactSheet-')):
        continue
    
    notContactSheetFilesList.append(notContactSheet)

for notContactSheets in (notContactSheetFilesList):
    try:
            matchImage = imageRegex.search(notContactSheets)
            imageCode = [matchImage.group(1)]
            imageCodesList.append(imageCode)
    except:
            matchImage = None
notContactSheetFilesList.sort()
#print(notContactSheetFilesList)

imageCodesList.sort()

for code in imageCodesList:
    if code not in imageCodes:
        imageCodes.append(code)

print(imageCodes)

index = 0

for contactSheets in (contactSheetList):
    print(contactSheets)

    newFileCode = str(imageCodes[index]) + 'Main.jpg';
    shutil.move(currentPath + '\\' + contactSheets, currentPath + '\\' + newFileCode)
    index += 1
