#!python3

import os, shutil
#model = 'IPHONE'
#os.chdir('D:\\Dropbox\Business\\Sublimation\\to do\\eBaySingleForMain\\1')
#os.chdir('D:\\Dropbox\Business\\Sublimation\\to do\\eBaySingleForMain\\2')
#os.chdir('D:\\Dropbox\Business\\Sublimation\\to do\\eBaySingleForMain\\3')
#os.chdir('D:\\Dropbox\Business\\Sublimation\\to do\\eBaySingleForMain\\4')

#model = 'WALLET'
#os.chdir('D:\\Dropbox\Business\\Sublimation\\to do\\eBaySingleWalletForMain\\1')
#os.chdir('D:\\Dropbox\Business\\Sublimation\\to do\\eBaySingleWalletForMain\\2')
#os.chdir('D:\\Dropbox\Business\\Sublimation\\to do\\eBaySingleWalletForMain\\3')
#os.chdir('D:\\Dropbox\Business\\Sublimation\\to do\\eBaySingleWalletForMain\\4')

model = 'Samsung'
##os.chdir('D:\\Dropbox\Business\\Sublimation\\to do\\ebaySingleForMainSamsung\\1-4\\1')
##os.chdir('D:\\Dropbox\Business\\Sublimation\\to do\\ebaySingleForMainSamsung\\1-4\\2')
##os.chdir('D:\\Dropbox\Business\\Sublimation\\to do\\ebaySingleForMainSamsung\\1-4\\3')
##os.chdir('D:\\Dropbox\Business\\Sublimation\\to do\\ebaySingleForMainSamsung\\1-4\\4')
##os.chdir('D:\\Dropbox\Business\\Sublimation\\to do\\ebaySingleForMainSamsung\\1-4\\5')
##os.chdir('D:\\Dropbox\Business\\Sublimation\\to do\\ebaySingleForMainSamsung\\5-8\\1')
##os.chdir('D:\\Dropbox\Business\\Sublimation\\to do\\ebaySingleForMainSamsung\\5-8\\2')
##os.chdir('D:\\Dropbox\Business\\Sublimation\\to do\\ebaySingleForMainSamsung\\5-8\\3')
##os.chdir('D:\\Dropbox\Business\\Sublimation\\to do\\ebaySingleForMainSamsung\\5-8\\4')


folderList = []
filesList = []

# Search for folders in directory & sort alphabetically
for files in (os.listdir('.')):
    if (files.endswith('.jpg')):
            continue
    folderList.append(files)    
    #print(files)        
folderList.sort()
#print(folderList)

# Search for images in directory & sort alphabetically
for files in (os.listdir('.')):
    if not (files.endswith('.jpg')):
            continue
    filesList.append(files)    
    #print(files)        
filesList.sort()
print(filesList)

#print(folderList[0])
print(filesList[0])
currentPath = os.path.abspath(os.getcwd())
print(currentPath)

# Loop through directory, find images, rename and move to correct folder
index = 0
for files in (filesList):
    shutil.move(currentPath + '\\' + files, currentPath + '\\' + folderList[index] + '\\'  + folderList[index] + 'Main' + model + '.jpg')
    print('Moving ' + currentPath + '\\' + files + ' to \n' + currentPath + '\\' + folderList[index] + '\\'  + folderList[index] + 'Main' + model + '.jpg' + '\n')
    index += 1
