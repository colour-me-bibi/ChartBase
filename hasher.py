import os
import hashlib


def hashAll(testFolder):
    for folder in os.listdir(testFolder):
        folderPath = os.path.join(testFolder, folder)
        renameFolder(folderPath, getHashForDir(folderPath))


def getHashForDir(folderPath):
    chart = None
    mid = None

    for f in os.listdir(folderPath):
        if f.endswith('.chart'):
            chart = f
        elif f.endswith('.mid'):
            mid = f

    if chart == None and mid == None:
        print(f'no file to hash exists in {folderPath}')
    elif chart == None:
        hasher = hashlib.md5()
        with open(os.path.join(folderPath, mid), 'rb') as hashFile:
            buf = hashFile.read()
            hasher.update(buf)
        return hasher.hexdigest()
    else:
        hasher = hashlib.md5()
        with open(os.path.join(folderPath, chart), 'rb') as hashFile:
            buf = hashFile.read()
            hasher.update(buf)
        return hasher.hexdigest()


def renameFolder(folderPath, folderHash):
    os.rename(folderPath, folderPath + ' md5=' + folderHash)
