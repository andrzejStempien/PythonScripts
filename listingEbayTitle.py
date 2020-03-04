import os, re, webbrowser, time, pyautogui

# directory for single images
dirSingImages = 'D:\\to do\\ebaySingleiPhone'
# directory for main images
dirMainImage = 'D:\\to do\\eBaySingleForMainiPhone'

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

# PHONE CASE COVER FOR APPLE iPhone

#For every main file in the list create a text file with item title
# user input max 80 characters
title = ''
for files in (mainList):
    titleFile = open(files + 'Title.txt', 'w')
    print('What is the title of the listing for ' + files + ' ? (max 80 characters)')
    while (len(title) > 80 or len(title) < 1):     
        title = input()
        title += ' PHONE CASE COVER FOR APPLE iPhone'
    print(title + ' was added to the file ' + (titleFile.name) + '.\n')
    titleFile.write(title)
    title = ''
    titleFile.close()
