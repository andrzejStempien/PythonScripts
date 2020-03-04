import os, re 

#dirTitle = 'D:\\Dropbox\Business\Sublimation\\to do\\eBaySingleWalletForMain'
dirTitle = 'D:\\Dropbox\Business\Sublimation\\to do\\ebaySingleForMainiPhone'

os.chdir(dirTitle)

# Loop through Title directory and find with title over 80 characters

for files in (os.listdir(dirTitle)):
    
    if not (files.endswith('Title.txt')):
        continue
    mainTitleFilePath = open(dirTitle + '\\' + files) #+ 'Title.txt'
    mainTitleFileContent = mainTitleFilePath.read()
    if (len(mainTitleFileContent) > 75):
        print('File ' + files + ' is ' + str(len(mainTitleFileContent)) + ' long.')
