from os import path
strPath = r"F:\Python Projects"
print('The current directory is: %s' % strPath)
print('Absolute Path is: %s' % path.abspath(strPath))
print('Basename is: %s' % path.basename(strPath))
print('isdir: %s' % path.isdir(strPath))
print('exists is: %s' % path.exists(strPath))
print('isfile is: %s' % path.isfile(strPath))
