Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import shutil, os
>>> os.chdir('C:\\')
>>> shutil.copy('C:\\spam.txt', 'C:\\delicious')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    shutil.copy('C:\\spam.txt', 'C:\\delicious')
  File "C:\Users\Andrzej\AppData\Local\Programs\Python\Python36-32\lib\shutil.py", line 241, in copy
    copyfile(src, dst, follow_symlinks=follow_symlinks)
  File "C:\Users\Andrzej\AppData\Local\Programs\Python\Python36-32\lib\shutil.py", line 120, in copyfile
    with open(src, 'rb') as fsrc:
FileNotFoundError: [Errno 2] No such file or directory: 'C:\\spam.txt'
>>> shutil.copy('C:\spam.txt', 'C:\\delicious')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    shutil.copy('C:\spam.txt', 'C:\\delicious')
  File "C:\Users\Andrzej\AppData\Local\Programs\Python\Python36-32\lib\shutil.py", line 241, in copy
    copyfile(src, dst, follow_symlinks=follow_symlinks)
  File "C:\Users\Andrzej\AppData\Local\Programs\Python\Python36-32\lib\shutil.py", line 120, in copyfile
    with open(src, 'rb') as fsrc:
FileNotFoundError: [Errno 2] No such file or directory: 'C:\\spam.txt'
>>> os.chdir('D:\\')
>>> shutil.copy('C:\\spam.txt', 'C:\\delicious')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    shutil.copy('C:\\spam.txt', 'C:\\delicious')
  File "C:\Users\Andrzej\AppData\Local\Programs\Python\Python36-32\lib\shutil.py", line 241, in copy
    copyfile(src, dst, follow_symlinks=follow_symlinks)
  File "C:\Users\Andrzej\AppData\Local\Programs\Python\Python36-32\lib\shutil.py", line 120, in copyfile
    with open(src, 'rb') as fsrc:
FileNotFoundError: [Errno 2] No such file or directory: 'C:\\spam.txt'
>>> shutil.copy('D:\\spam.txt', 'D:\\delicious')
'D:\\delicious'
>>> shutil.copy('D:\\spam.txt', 'D:\\delicious')
'D:\\delicious\\spam.txt'
>>> shutil.copy('eggs.txt', 'C:\\delicious\\eggs2.txt')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    shutil.copy('eggs.txt', 'C:\\delicious\\eggs2.txt')
  File "C:\Users\Andrzej\AppData\Local\Programs\Python\Python36-32\lib\shutil.py", line 241, in copy
    copyfile(src, dst, follow_symlinks=follow_symlinks)
  File "C:\Users\Andrzej\AppData\Local\Programs\Python\Python36-32\lib\shutil.py", line 120, in copyfile
    with open(src, 'rb') as fsrc:
FileNotFoundError: [Errno 2] No such file or directory: 'eggs.txt'
>>> shutil.copy('eggs.txt', 'D:\\delicious\\eggs2.txt')
'D:\\delicious\\eggs2.txt'
>>> 
>>> 
>>> import shutil, os
>>> os.chdir('D:\\')
>>> shutil.copytree('C:\\bacon', 'C:\\bacon_backup')
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    shutil.copytree('C:\\bacon', 'C:\\bacon_backup')
  File "C:\Users\Andrzej\AppData\Local\Programs\Python\Python36-32\lib\shutil.py", line 309, in copytree
    names = os.listdir(src)
FileNotFoundError: [WinError 3] The system cannot find the path specified: 'C:\\bacon'
>>> shutil.copytree('D:\\bacon', 'D:\\bacon_backup')
'D:\\bacon_backup'
>>> import shutil
>>> shutil.move('D:\\bacon.txt', 'D:\\eggs')
'D:\\eggs'
>>> shutil.move('D:\\bacon.txt', 'D:\\eggs')
'D:\\eggs\\bacon.txt'
>>> 
>>> shutil.move('D:\\bacon.txt', 'D:\\eggs\\new_bacon.txt')
'D:\\eggs\\new_bacon.txt'
>>> 
>>> shutil.move('spam.txt;, 'D:\\does_not_extist\\eggs\ham')
		
SyntaxError: invalid syntax
>>> shutil.move('spam.txt', 'D:\\does_not_extist\\eggs\ham')
		
Traceback (most recent call last):
  File "C:\Users\Andrzej\AppData\Local\Programs\Python\Python36-32\lib\shutil.py", line 544, in move
    os.rename(src, real_dst)
FileNotFoundError: [WinError 3] The system cannot find the path specified: 'spam.txt' -> 'D:\\does_not_extist\\eggs\\ham'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    shutil.move('spam.txt', 'D:\\does_not_extist\\eggs\ham')
  File "C:\Users\Andrzej\AppData\Local\Programs\Python\Python36-32\lib\shutil.py", line 558, in move
    copy_function(src, real_dst)
  File "C:\Users\Andrzej\AppData\Local\Programs\Python\Python36-32\lib\shutil.py", line 257, in copy2
    copyfile(src, dst, follow_symlinks=follow_symlinks)
  File "C:\Users\Andrzej\AppData\Local\Programs\Python\Python36-32\lib\shutil.py", line 121, in copyfile
    with open(dst, 'wb') as fdst:
FileNotFoundError: [Errno 2] No such file or directory: 'D:\\does_not_extist\\eggs\\ham'
>>> 
		
>>> os.unlink('D:\\bacon')
		
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    os.unlink('D:\\bacon')
PermissionError: [WinError 5] Access is denied: 'D:\\bacon'
>>> os.rndir('D:\\bacon')
		
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    os.rndir('D:\\bacon')
AttributeError: module 'os' has no attribute 'rndir'
>>> os.rmdir('D:
	     
SyntaxError: EOL while scanning string literal
>>> 
	     
>>> os.rmdir('D:\\bacon')
	     
>>> shutil.rmtree('D:\\delicious\\')
	     
>>> 
	     
>>> import send2trash
	     
>>> baconFile = open('bacon.txt', 'a') # creates the file
	     
>>> baconFile.write('Bacon is not a vegetable.;)
		    
SyntaxError: EOL while scanning string literal
>>> baconFile.write('Bacon is not a vegetable.')
		    
25
>>> baconFile.close()
		    
>>> send2trash.send2trash('bacon.txt')
		    
>>> 
============= RESTART: D:/Dropbox/MyPythonScripts/treeWalking.py =============
The current folder is D:\delicious
SUBFOLDER OF D:\delicious: cats
SUBFOLDER OF D:\delicious: walnut
FILE INSIDE D:\delicious: spam.txt
 
The current folder is D:\delicious\cats
FILE INSIDE D:\delicious\cats: catnames.txt
FILE INSIDE D:\delicious\cats: zophie.jpg
 
The current folder is D:\delicious\walnut
SUBFOLDER OF D:\delicious\walnut: waffles
 
The current folder is D:\delicious\walnut\waffles
FILE INSIDE D:\delicious\walnut\waffles: butter.txt
 
>>> 
		    
>>> import zipfile, os
		    
>>> os.chdir('D:\\')	# move to the folder with example.zip
