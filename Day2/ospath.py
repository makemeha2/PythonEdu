from os.path import *
import glob

print(dirname('C:\examples\Day2\ospath.py'))
print(exists('C:\examples\Day2\ospath.py'))
print(expanduser('~\\test'))
print(expandvars('$SYSTEMROOT\\VAR'))
print(glob.glob('*'))
