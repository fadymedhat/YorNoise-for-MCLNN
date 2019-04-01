import os
from fnmatch import fnmatch


SRC_PATH = 'F:/YorNoise/YorNoise'
SCRIPT_FILE_NAME = 'id_01_resample_22050_wav.bat'

f = open(SCRIPT_FILE_NAME, 'w')
f.write(':: This file is used to resample URBANSOUND8k to 22050 sampling rate wav\n')
f.write(':: make sure to configure the source and destination folders and have ffmpeg installed before your execute this script\n')
f.write(':: Fady Medhat\n')
f.write(':: version 0.1\n')
f.write('@echo off\n')
f.write('set src_location=I:\\SOURCE\\PATH\n')
f.write('set dst_location=I:\\DESTINATION\\PATH\n')
f.write('C:\n')
f.write('IF NOT EXIST %dst_location% (\n')
f.write('echo Create %dst_location% first!\n')
f.write('GOTO EOF\n')
f.write(')\n')
f.write('xcopy /t /e "%src_location%" "%dst_location%"\n')

filePathString = []
scriptLine = []
for path, subdirs, files in sorted(os.walk(SRC_PATH,topdown=False)):
    for name in sorted(files):
        if fnmatch(name, "*.wav"):
            filePathString = os.path.join(path,name)
            scriptLine = 'ffmpeg -y -i "%src_location%\\' + os.path.join(os.path.basename(path),name) + '" -ab 128k -acodec pcm_s16le -ac 1 -ar 22050 "%dst_location%\\'+ os.path.join(os.path.basename(path),name) + '"\n'
            os.path.basename(path)
            f.write(scriptLine)
f.write(':EOF\n')


#URBAN = 'I:/UrbanSound8KexpandedSmallfiles/urban_york'



#f = open('ffmpegmp3towavUrbanSoundk8_22050York.txt', 'w')
# filePathString = []
# scriptLine = []
# for path, subdirs, files in sorted(os.walk(URBAN,topdown=False)):
#     for folder in sorted (subdirs):
#         categoryFolder = os.path.join( URBAN,folder)
#         for path, subdirs, files in sorted(os.walk(categoryFolder, topdown=False)):
#             for folder in sorted(subdirs):
#                 for path, subdirs, files in sorted(os.walk(os.path.join(categoryFolder, folder), topdown=False)):
#                     for name in sorted(files):
#                         if fnmatch(name, "*.wav"): #*.mp3 au"
#                             filePathString = path + '\\' + name
#                             dstFilePathString = categoryFolder.replace('urban_york', 'audiostretch')+ '\\' + name
#                             scriptLine = 'ffmpeg -y -i "' + filePathString + '" -ab 128k -acodec pcm_s16le -ac 1 -ar 22050 "'+ dstFilePathString + '"\n'
#                             f.write(scriptLine)