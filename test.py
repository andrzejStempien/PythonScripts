import os, re
dirSingImages = 'D:\\Dropbox\Business\Sublimation\\to do\\ebaySingle'

phoneCaseImagesList = []
singleImageRegex = re.compile('AIW01\d')

for files in (os.listdir(dirSingImages)):
        if not (files.endswith('.jpg')):
            continue
        #print(files)
        try:
            matchSingleImage = singleImageRegex.search(files)
            #print(matchSingleImage.group())
            phoneCaseImagesList.append(matchSingleImage.group())
        except:
            matchMainImage = None        
        phoneCaseImagesList.sort()
        
print(phoneCaseImagesList)
