import os
from os.path import isfile ,join
import shutil


file_path = os.getcwd()

DOCUMENTS = ('txt', 'doc', 'docx', 'pdf', 'odt', 'rtf', 'ppt', 'pptx', 'xls', 'xlsx', 'csv')
VIDEO = ('mp4', 'avi', 'mkv', 'mov', 'wmv', 'flv', 'webm', 'm4v', '3gp', 'mpeg', 'mpg')
AUDIO = ('mp3', 'wav', 'flac', 'aac', 'ogg', 'wma', 'm4a', 'aiff', 'opus', 'alac', 'pcm')
PICTURES = ('jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp', 'svg')
EXCECUTABLES = ('exe', 'dll', 'bat', 'com', 'sh', 'app', 'msi', 'jar', 'run', 'deb')

files = [f for f in os.listdir(file_path) if isfile(join(file_path, f))]

def organizer(file_type):
    for file in files:
        archive = file.split('.')
        if archive[1] in file_type:
            print(file)

