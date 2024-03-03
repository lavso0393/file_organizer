import os
from os.path import isfile ,join, isdir
import shutil


file_path = os.getcwd()+'/'

DOCUMENTS = ('txt', 'doc', 'docx', 'pdf', 'odt', 'rtf', 'ppt', 'pptx', 'xls', 'xlsx', 'csv')
VIDEO = ('mp4', 'avi', 'mkv', 'mov', 'wmv', 'flv', 'webm', 'm4v', '3gp', 'mpeg', 'mpg')
AUDIO = ('mp3', 'wav', 'flac', 'aac', 'ogg', 'wma', 'm4a', 'aiff', 'opus', 'alac', 'pcm')
PICTURES = ('jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp', 'svg')
EXCECUTABLES = ('exe', 'dll', 'bat', 'com', 'sh', 'app', 'msi', 'jar', 'run', 'deb')
COMPRESSED = ('zip', 'rar', '7z', 'tar', 'gz', 'bz2', 'xz', 'tgz', 'iso')

categories = {"DOCUMENTS":DOCUMENTS, "VIDEO":VIDEO, "AUDIO":AUDIO, "PICTURES":PICTURES, 
              "EXCECUTABLES":EXCECUTABLES, "COMPRESSED":COMPRESSED}

files = [f for f in os.listdir(file_path) if isfile(join(file_path, f))]

def organizer(file_path, file_type=None, folder_name= 'OTHERS'):
    """Organize the files in the current folder"""
    for file in files:
        dest_path = file_path + folder_name
        archive = file.split('.')
        if file_type is None:
            if not isdir(dest_path):
                os.mkdir(dest_path)
            src_path  = file_path + file
            dest_path += '/' + file
            shutil.move(src_path, dest_path) 
        else:
            if archive[-1].lower() in file_type:
                if not isdir(dest_path):
                    os.mkdir(dest_path)
                src_path  = file_path + file
                dest_path += '/' + file
                shutil.move(src_path, dest_path)  


for name, category in categories.items():
    organizer(file_path, category, name)
    
files = [f for f in os.listdir(file_path) if isfile(join(file_path, f))]
organizer(file_path)
