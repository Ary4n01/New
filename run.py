import platform
print('\033[0;1m[\033[1;30m•\033[0;1m]\033[0;1mLOADING')
#print('\033[0;1m[\033[1;30m•\033[0;1m]\033[0;1mCHECKING FOR UPDATES')
bit = platform.architecture()[0]
if bit == '64bit':
    print('\033[0;1m[\033[1;30m•\033[0;1m]\033[0;1m64BIT DETECTED')
    import new_64
elif bit == '32bit':
    print ('\033[0;1m[\033[1;30m•\033[0;1m]\033[0;1m32BIT DETECTED')
    import new_32
