import wget
import urllib.parse
import json
import re
import threading
import os
import config
import hashlib
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Updates a downloaded record
def writeLine(url):
    with open('downloaded.txt', 'a') as writeFile:
        writeFile.write(url + '\n')

# Downloads files from Google Drive
def gDriveDownload(drive, url):
    fileID = re.search(r'//.*(?:/folders|/d)/([^/,\n]*)', url).group(1)

    driveFile = drive.CreateFile({'id': fileID})

    if 'folder' in driveFile['mimeType']:
        fileList = drive.ListFile(
            {'q': "'{}' in parents and trashed=false".format(fileID)}).GetList()

        nestedDir = f"/disks/Benny2TB/db/downloaded/{driveFile['title']}"

        if not os.path.exists(nestedDir):
            os.makedirs(nestedDir)

        for siblingFile in fileList:
            if 'folder' not in siblingFile['mimeType']:
                siblingFile.GetContentFile(
                    f"{nestedDir}/{siblingFile['title']}", mimetype=siblingFile['mimeType'])

        writeLine(url)
    else:
        driveFile.GetContentFile(
            f"/disks/Benny2TB/db/downloaded/{driveFile['title']}", mimetype=driveFile['mimeType'])
        writeLine(url)

# Downloads normal files
def downloadDirect(url):
    wget.download(url, '/disks/Benny2TB/db/downloaded')
    writeLine(url)

# TODO link to sqlite db instead of urls record
def startDownloads():
    # Google Drive authentication
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()  # Needed only for initial auth
    drive = GoogleDrive(gauth)

    with open('songs-20191009.jsonl') as file:
        for line in file:
            lineJSON = json.loads(line)

            url = urllib.parse.unquote(lineJSON['url'])

            domain = re.search(r'.*?://(.*?)/', url).group(1)

            if 'drive.google' in domain:
                try:
                    gDriveDownload(drive, url)
                except (KeyboardInterrupt, SystemExit):
                    raise
                except:
                    print(f'Could not download {url}')
                    with open('rejects.jsonl', 'a') as rejectsFile:
                        rejectsFile.write(url + '\n')
                # THREADING !!! Google don't like !!!
                # gThread = threading.Thread(target=gDriveDownload, args=[url])
                # gThread.start()
            else:
                try:
                    downloadDirect(url)
                except (KeyboardInterrupt, SystemExit):
                    raise
                except:
                    print(f'Could not download {url}')
                    with open('rejects.jsonl', 'a') as rejectsFile:
                        rejectsFile.write(url + '\n')
                # THREADING !!! I'm scared !!!
                # dThread = threading.Thread(target=download(url), args=[url])
                # dThread.start()


# Remove downloaded urls from master record
def cleanDownloadRecord():
    with open('downloaded.txt') as masterFile:
    for masterLine in masterFile:
        with open('songs-20191009.jsonl', 'r') as readFile:
            lines = readFile.readlines()
        with open('songs-20191009.jsonl', 'w') as writeFile:
            for line in lines:
                lineJSON = json.loads(line)
                if masterLine.strip('\n') != urllib.parse.unquote(lineJSON['url']):
                    writeFile.write(line)

# Return hash of the chart or mid file for a given folder
def getHashForFolder(folderPath):
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

# Renames a folder with a hash
def appendHashToFolder(folderPath, folderHash):
    os.rename(folderPath, folderPath + ' md5=' + folderHash)


def appendHashToAllFolders(testFolder):
    for folder in os.listdir(testFolder):
        folderPath = os.path.join(testFolder, folder)
        appendHashToFolder(folderPath, getHashForFolder(folderPath))

# TODO change this to update a SQLite db with downloaded boolean
