import subprocess
import sys
import os


print('TEST') 
python_exe = os.path.join(sys.prefix, 'bin', 'python.exe')
target = os.path.join(sys.prefix, 'lib', 'site-packages')
 
subprocess.call([python_exe, '-m', 'ensurepip'])
subprocess.call([python_exe, '-m', 'pip', 'install', '--upgrade', 'pip'])
 
subprocess.call([python_exe, '-m', 'pip', 'install', '--upgrade', 'scipy', '-t', target])
 
print('FINISHED')



#import subprocess
#import sys
#import os
# 
## path to python.exe
#python_exe = os.path.join(sys.prefix, 'bin', 'python.exe')
# 
## upgrade pip
#subprocess.call([python_exe, "-m", "ensurepip"])
#subprocess.call([python_exe, "-m", "pip", "install", "--upgrade", "pip"])
# 
## install required packages
#subprocess.call([python_exe, "-m", "pip", "install", "package_name"])
