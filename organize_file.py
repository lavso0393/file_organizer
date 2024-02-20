import os
from os.path import isfile ,join, isdir
import shutil

file_path = "/mnt/c/Users/osval/Downloads/"
#file_path = os.getcwd()

DOCUMENTS = ('txt', 'doc', 'docx', 'pdf', 'odt', 'rtf', 'ppt', 'pptx', 'xls', 'xlsx', 'csv')
VIDEO = ('mp4', 'avi', 'mkv', 'mov', 'wmv', 'flv', 'webm', 'm4v', '3gp', 'mpeg', 'mpg')
AUDIO = ('mp3', 'wav', 'flac', 'aac', 'ogg', 'wma', 'm4a', 'aiff', 'opus', 'alac', 'pcm')
PICTURES = ('jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp', 'svg')
EXCECUTABLES = ('exe', 'dll', 'bat', 'com', 'sh', 'app', 'msi', 'jar', 'run', 'deb')
COMPRESSED = ('zip', 'rar', '7z', 'tar', 'gz', 'bz2', 'xz', 'tgz', 'tar.gz', 'tar.bz2', 'tar.xz', 'iso')

files = [f for f in os.listdir(file_path) if isfile(join(file_path, f))]

def organizer(file_path, file_type, folder_name= 'OTHERS'):
    for file in files:
        dest_path = file_path + folder_name
        archive = file.split('.')
        if archive[1].lower() in file_type:
            if not isdir(dest_path):
                os.mkdir(dest_path)
            src_path  = file_path + file
            dest_path += '/' + file
            shutil.move(src_path, dest_path)  


organizer(file_path, COMPRESSED)