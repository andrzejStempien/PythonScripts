#! python3 //moves all files in folder that are named in format DDDD000 to the right folders

import os, re, shutil

os.chdir('D:\Dropbox\Business\\Sublimation\\3. All models ready to print')

# Regex for image code
imageRegex = re.compile(r'((\w)+)(\d\d)\d')               
filesList = []

#Search directory for .jpg files that match format
for files in (os.listdir('.')):
    if not (files.endswith('iPhone 7 PLUS.jpg')):
            continue
    try:
        #matchImage = imageRegex.search(files)
        #os.makedirs(os.getcwd() + '\\' + matchImage.group(1) + matchImage.group(3) + '\\')
        shutil.move('D:\Dropbox\\Business\\Sublimation\\3. All models ready to print\\' + files, 'D:\Dropbox\\Business\\Sublimation\\3. All models ready to print\\iPhone 7 PLUS\\' + files)
    except:
        matchImage = None
##        
##for files in (os.listdir('.')):
##    if not (files.endswith('.jpg')):
##            continue
##    try:
##        matchImage = imageRegex.search(files)
##        #print(matchImage.group(1) + matchImage.group(3))
##        #print(matchImage.group(3))
##        #print(os.getcwd() + '\\' + matchImage.group(1) + matchImage.group(3))
##        #shutil.move('D:\Dropbox\Business\Sublimation\\to do\\eBaySingleWalletForMain\\' + matchImage.group() + '.jpg', 'D:\Dropbox\Business\Sublimation\\to do\\eBaySingleWalletForMain\\' + matchImage.group(1) + matchImage.group(3) + '\\' + matchImage.group() + '.jpg')
##        shutil.move('D:\Dropbox\\Business\\Sublimation\\3. All models ready to print\\iPhone 6' + files, 'D:\Dropbox\\Business\\Sublimation\\3. All models ready to print\\iPhone 6' + files)
##        print('Moving file..  ' + matchImage.group() + '.jpg')
##    except:
##        matchImage = None
