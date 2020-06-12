# List directory contents
import os
spath = r"E:\TAP TAP\Launch\Extension\LUMS EMAIL LIST\RESUMES-Class of 2020\MUSHTAQ AHMAD GURMANI SCHOOL OF HUMANITIES AND SOCIAL SCIENCES\Graduates\MS Economics 2.5 Years"
# Everything
print(os.listdir(spath))
# Get Everything Split
# for roots, dirs, files in os.walk(spath):
#    for dir in dirs:
#        print("dir = %s" % dirs)

# Only the roots
roots = next(os.walk(spath))[0]
print("Roots = %s" % roots)

# Only the dirs
dirs = next(os.walk(spath))[1]
print("Dirs = %s" % dirs)

# Only the files
files = next(os.walk(spath))[2]
print("Files = %s" % files)
